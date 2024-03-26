from oscar.apps.checkout.views import ShippingMethodView as ParentShippingMethodView
from base.models import ShippingMethod
from oscar.core.loading import get_model

UserAddress = get_model('address', 'UserAddress')
class ShippingMethodView(ParentShippingMethodView):    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["methods"] = self._methods
        shipping_address_country = self.get_shipping_address(basket=self.request.basket).country
        parents_node = ShippingMethod.objects.filter(child_of__isnull=True, countries=shipping_address_country)
        checkpoint_node = {}
        # print(UserAddress.objects.filter(user=self.request.user))

        if parents_node:
            for i in parents_node:
                all_ids = ShippingMethod.objects.filter(child_of__id = i.id, countries=shipping_address_country)
                checkpoint_node[i.id] = [x.name for x in all_ids]

        kwargs['checkpoint_node'] = checkpoint_node
        kwargs['parents_node'] = parents_node
        print(parents_node)
        return kwargs
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["methods"] = self._methods
        return kwargs