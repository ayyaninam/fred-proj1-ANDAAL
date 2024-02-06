from oscar.apps.checkout.views import ShippingMethodView as ParentShippingMethodView
from base.models import ShippingMethod
class ShippingMethodView(ParentShippingMethodView):    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["methods"] = self._methods
        parents_node = ShippingMethod.objects.filter(child_of__isnull=True)
        checkpoint_node = {}
        if parents_node:
            for i in parents_node:
                all_ids = ShippingMethod.objects.filter(child_of__id = i.id)
                checkpoint_node[i.id] = [x.name for x in all_ids]

        kwargs['checkpoint_node'] = checkpoint_node
        kwargs['parents_node'] = parents_node
        return kwargs
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["methods"] = self._methods
        return kwargs