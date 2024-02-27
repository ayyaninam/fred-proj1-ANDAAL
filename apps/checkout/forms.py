from oscar.apps.checkout.forms import ShippingAddressForm as ParentShippingAddressForm
from oscar.core.loading import get_model

class ShippingAddressForm(ParentShippingAddressForm):
    class Meta:
        model = get_model("order", "shippingaddress")
        labels = {
            "line1": "Complete Address"
        }
        fields = [
            "first_name",
            "last_name",
            "line1",
            # "line2",
            # "line3",
            "line4",
            "state",
            "postcode",
            "country",
            "phone_number",
            "notes",
        ]