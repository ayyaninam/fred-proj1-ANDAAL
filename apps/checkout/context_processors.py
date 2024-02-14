from django.conf import settings # import the settings file

def default_currency(request):
    return {'OSCAR_DEFAULT_CURRENCY': settings.OSCAR_DEFAULT_CURRENCY}

def openinhttps(request):
    return {'OPEN_IN_HTTPS': settings.PAYPAL_CALLBACK_HTTPS}