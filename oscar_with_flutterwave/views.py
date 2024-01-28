from django.shortcuts import render
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from .flutterPaymentLogic import Facade
# Create your views here.

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from oscar.core.exceptions import ModuleNotFoundError
from oscar.core.loading import get_class, get_model
from oscar_stripe_sca.facade import logger
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from oscar_with_flutterwave.flutterPaymentLogic import Facade
from . import PAYMENT_EVENT_PURCHASE, PAYMENT_METHOD_FLUTTERFLOW

SourceType = get_model('payment', 'SourceType')
Source = get_model('payment', 'Source')
Line = get_model('basket', 'Line')
Basket = get_model('basket', 'Basket')
Selector = get_class('partner.strategy', 'Selector')
try:
    Applicator = get_class('offer.applicator', 'Applicator')
except ModuleNotFoundError:
    # fallback for django-oscar<=1.1
    Applicator = get_class('offer.utils', 'Applicator')


class FlutterWavePaymentDetail(CorePaymentDetailsView):
    template_name = "oscar/checkout/flutterwave_payment_details_input.html"

    def get_context_data(self, **kwargs):
        ctx = super(FlutterWavePaymentDetail, self).get_context_data(**kwargs)
        # print(ctx)
        flutter_payload = Facade().begin(
            ctx["basket"],
            ctx["order_total"])

        self.request.session["flutter_payload"] = flutter_payload
        return ctx

class FlutterMakePayment(CorePaymentDetailsView):
    preview = True
    template_name_preview = 'oscar/checkout/flutterwave_payment_details_view.html'

    @property
    def pre_conditions(self):
        return []

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FlutterMakePayment, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        
        ctx = super(FlutterMakePayment, self).get_context_data(**kwargs)
        # print(ctx)
        if ctx['order_total'] is None:
            messages.error(self.request, "Your checkout session has expired, please try again")
            raise PermissionDenied
        else:
            ctx['order_total_incl_tax_cents'] = (
                ctx['order_total'].incl_tax * 100
            ).to_integral_value()
            
        return ctx

    def handle_payment(self, order_number, order_total, **kwargs):

        payload = None
        mobile_number_flutterflow = None
        try:
            mobile_number_flutterflow = self.request.GET.get('mobile_number_flutterflow')
            if mobile_number_flutterflow:
                payload = self.request.session['flutter_payload']
                payload['phone_number'] = mobile_number_flutterflow
                # payload['currency'] = 'XAF'
            else:
                raise Exception("No Mobile Number Provided")
        except:
            raise Exception("No Payloads please try again")

        response = Facade().capture(order_number, payload=payload)
        pi = response.json()['data']['tx_ref']

        source_type, __ = SourceType.objects.get_or_create(name=PAYMENT_METHOD_FLUTTERFLOW)
        source = Source(
            source_type=source_type,
            currency=settings.STRIPE_CURRENCY,
            amount_allocated=order_total.incl_tax,
            amount_debited=order_total.incl_tax,
            reference=pi)
        
        self.add_payment_source(source)

        self.add_payment_event(PAYMENT_EVENT_PURCHASE, order_total.incl_tax, reference=pi)

        del self.request.session["flutter_payload"]

    def payment_description(self, order_number, total, **kwargs):
        return "Mobile payment for order {0} by {1}".format(order_number, self.request.user.get_full_name())

    @staticmethod
    def payment_metadata(order_number, total, **kwargs):
        return {
            'order_number': order_number,
        }

    def load_frozen_basket(self, basket_id):
        # Lookup the frozen basket that this txn corresponds to
        try:
            basket = Basket.objects.get(id=basket_id, status=Basket.FROZEN)
        except Basket.DoesNotExist:
            return None

        # Assign strategy to basket instance
        if Selector:
            basket.strategy = Selector().strategy(self.request)

        # Re-apply any offers
        Applicator().apply(basket, self.request.user, request=self.request)

        return basket

    def get(self, request, *args, **kwargs):
        kwargs['basket'] = self.load_frozen_basket(kwargs['basket_id'])
        if not kwargs['basket']:
            logger.warning(
                "Unable to load frozen basket with ID %s", kwargs['basket_id'])
            messages.error(
                self.request,
                _("No basket was found that corresponds to your "
                  " transaction"))
            return HttpResponseRedirect(reverse('basket:summary'))
        
        return super(FlutterMakePayment, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Place an order.
        """
        # Reload frozen basket which is specified in the URL

        basket = self.load_frozen_basket(kwargs['basket_id'])
        if not basket:
            messages.error(self.request, _("No basket was found that corresponds to your "
                "Francophone mobile money transaction"))
            return HttpResponseRedirect(reverse('basket:summary'))

        submission = self.build_submission(basket=basket)
        return self.submit(**submission)


