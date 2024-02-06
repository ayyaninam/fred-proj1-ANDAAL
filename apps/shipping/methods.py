from oscar.apps.shipping import methods
from oscar.core import prices
from decimal import Decimal as D


# Home delivery or pick-up delivery
# class HomeDelivery(methods.Base):
#     code = 'homedelivery'
#     name = 'Home Delivery'

#     def calculate(self, basket):
#         return prices.Price(
#             currency=basket.currency,
#             excl_tax=D('10.00'), incl_tax=D('10.00'))

    
# class PickUpDelivery(methods.Base):
#     code = 'pickupdelivery'
#     name = 'Pick-up Delivery'

#     def calculate(self, basket):
#         return prices.Price(
#             currency=basket.currency,
#             excl_tax=D('0.00'), incl_tax=D('0.00'))
    
class DeliveryMaker(methods.Base):
    def __init__(self, _code, _name, _charge_excl_tax, _charge_incl_tax):
        self.code = _code
        self.name = _name
        self.charge_excl_tax = D(_charge_excl_tax)
        self.charge_incl_tax = D(_charge_incl_tax)

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D(self.charge_incl_tax), incl_tax=D(self.charge_incl_tax))
