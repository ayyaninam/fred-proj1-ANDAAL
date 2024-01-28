import oscar.apps.checkout.apps as apps
from oscar.core.loading import get_class
from django.urls import path


class CheckoutConfig(apps.CheckoutConfig):
    name = 'apps.checkout'

    def ready(self):
        from oscar_stripe_sca import views as stripe_sca_views
        from oscar_with_flutterwave import views as fluter_wave_view
        super().ready()
        self.stripe_payment_details_view = stripe_sca_views.StripeSCAPaymentDetailsView
        self.stripe_preview = stripe_sca_views.StripeSCASuccessResponseView
        self.stripe_cancel_preview = stripe_sca_views.StripeSCASuccessResponseView

        self.flutter_wave_payment_detail_input = fluter_wave_view.FlutterWavePaymentDetail
        self.flutter_wave_payment_detail_view = fluter_wave_view.FlutterMakePayment


    def get_urls(self):
        urls = super(CheckoutConfig, self).get_urls()
        urls += [
            path("stripe-payment-detail-view/", self.stripe_payment_details_view.as_view(), name="stripe_payment_details_view"),
            path("flutter-wave-payment-detail-input/", self.flutter_wave_payment_detail_input.as_view(), name="flutter_wave_payment_detail_input"),
            path("flutter-wave-payment-detail-view/<int:basket_id>/", self.flutter_wave_payment_detail_view.as_view(), name="flutter_wave_payment_detail_view"),
        ]

        return urls
