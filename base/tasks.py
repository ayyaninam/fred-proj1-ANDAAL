from celery import shared_task 
from django.conf import settings
from .models import *
import requests

@shared_task
def my_task():
    resp = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={settings.EXCHANGE_RATE_API_KEY}')
    all_rates = RateOfEuro.objects.all()
    
    if all_rates.count() > 9:
        for i in all_rates[9:]:
            i.delete()
            
    if resp.status_code == 200:
        print("RUN")
        RateOfEuro.objects.create(base="EUR", xaf_to_euro=float(1/float(resp.json()['rates'][f'{settings.OSCAR_DEFAULT_CURRENCY}'])))
    
    return "Currencies EXCHANGE RATE Updated!"