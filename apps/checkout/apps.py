import oscar.apps.checkout.apps as apps
from oscar.core.loading import get_class
from django.urls import path


class CheckoutConfig(apps.CheckoutConfig):
    name = 'apps.checkout'
    # def ready(self):
    #     self.stripe_payment_handle = get_class("checkout.views", "stripe_payment_handle")

    # def get_urls(self):
    #     urls = [
    #         path("stripe-payment-handle/", self.stripe_payment_handle.as_view(), name="stripe_payment_handle"),
    #     ],

    #     return self.post_process_urls(urls)


    def ready(self):
        from oscar_stripe_sca import views as stripe_sca_views
        super().ready()
        self.payment_details_view = stripe_sca_views.StripeSCAPaymentDetailsView
        self.stripe_preview = stripe_sca_views.StripeSCASuccessResponseView
        self.stripe_cancel_preview = stripe_sca_views.StripeSCASuccessResponseView

    # def get_urls(self):
    #     urls = [
    #         path("payment-details-view/", self.payment_details_view_1.as_view(), name="payment_details_view"),
    #     ]
    #     return self.post_process_urls(urls)

    # def get_urls(self):
    #     urls = [
    #         path(
    #             "preview-stripe/",
    #             self.payment_details_view.as_view(preview=True),
    #             name="preview",
    #         ),
    #     ]
    #     return self.post_process_urls(urls)



