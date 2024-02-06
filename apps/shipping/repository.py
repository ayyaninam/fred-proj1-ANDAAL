from oscar.apps.shipping import repository
from . import methods as outer_method
from decimal import Decimal as D
from base.models import ShippingMethod
class Repository(repository.Repository):

    methods = [outer_method.DeliveryMaker(x.code,x.name,x.charge_excl_tax,x.charge_incl_tax) for x in ShippingMethod.objects.filter(child_of__isnull=False)]
    methods = tuple(methods)
