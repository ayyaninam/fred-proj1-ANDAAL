from django.conf import settings
from django.contrib.sites.models import Site
from django.apps import apps
import logging
import uuid
import requests


logger = logging.getLogger(__name__)
Source = apps.get_model('payment', 'Source')
Order = apps.get_model('order', 'Order')

ZERO_DECIMAL_CURRENCIES = (
    'BIF',  # Burundian Franc
    'CLP',  # Chilean Peso
    'DJF',  # Djiboutian Franc
    'GNF',  # Guinean Franc
    'JPY',  # Japanese Yen
    'KMF',  # Comorian Franc
    'KRW',  # South Korean Won
    'MGA',  # Malagasy Ariary
    'PYG',  # Paraguayan Guaraní
    'RWF',  # Rwandan Franc
    'VND',  # Vietnamese Đồng
    'VUV',  # Vanuatu Vatu
    'XAF',  # Central African Cfa Franc
    'XOF',  # West African Cfa Franc
    'XPF',  # Cfp Franc
)


class Facade(object):
    def __init__(self):
        pass

    @staticmethod
    def get_friendly_decline_message(error):
        return 'The transaction was declined by your bank - please check your bankcard details and try again'

    @staticmethod
    def get_friendly_error_message(error):
        return 'An error occurred when communicating with the payment gateway.'

    def begin(self, basket, total):
        multiplier = 1
        if total.currency.upper() in ZERO_DECIMAL_CURRENCIES:
            multiplier = 1
        else:
            multiplier = 100

        site = Site.objects.get_current()
        line_items_summary = ", ".join(["{0}x{1}".format(l.quantity, l.product.title) for l in basket.lines.all()])

        # basket.freeze()

        payload = {
            "tx_ref":str(uuid.uuid4()),
            "amount":int(multiplier * total.incl_tax),
            "currency":total.currency.upper(),
            "country": "CM",
            "email":basket.owner.email,
            "phone_number":"08000000000",
            "fullname":basket.owner.get_full_name()
        }

        return payload


    def capture(self, order_number, payload, **kwargs):

        logger.info("Initiating payment capture for order '%s' via FlutterFlow" % (order_number))

        # try:


        # {"status":"error","message":"Please specify the following parameters in body: amount, tx_ref, email, phone_number, currency","data":null}
        
        headers = {
        'Authorization': settings.FLUTTER_WAVE_SCRETE_KEY,
        'content-type':'application/json'
        }
        
        resp = requests.post(settings.FLUTTER_PAYMENT_URL, json=payload, headers=headers)
        if resp.status_code == 200:
                logger.exception('Payment Complete for order no. : \'{}\''.format(order_number) )
                return resp
        else:
            raise Exception("Capture Failure could not find payment source for Order %s" % order_number)
           
        # except Source.DoesNotExist as e:
        #     logger.exception('Source Error for order: \'{}\''.format(order_number) )
        #     raise Exception("Capture Failure could not find payment source for Order %s" % order_number)
        # except Order.DoesNotExist as e:
        #     logger.exception('Order Error for order: \'{}\''.format(order_number) )
        #     raise Exception("Capture Failure Order %s does not exist" % order_number)
