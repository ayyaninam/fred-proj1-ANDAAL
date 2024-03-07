
from pathlib import Path
import os
# django oscar

from oscar.defaults import *



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qo(wyxti=gh@owlvjfg90kelac!(nb(xc$hpn7l9y$i+^l6hc*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'oscar_stripe_sca',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'django.contrib.sites',
    'django.contrib.flatpages',


# django oscar

    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    # Start Changed
    'apps.checkout.apps.CheckoutConfig',
    # End Changed

    'oscar.apps.address.apps.AddressConfig',
    'apps.shipping.apps.ShippingConfig',
    'apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    # 'oscar.apps.customer.apps.CustomerConfig',
    'apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',

    # payment integrations
    'paypal',
    'oscar_with_flutterwave',
    'django_oscar_stripe_sca',
    'base.apps.BaseConfig',
    'django_celery_beat',
    'django_celery_results',
] 

SITE_ID = 1
AUTH_USER_MODEL = "base.User"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
# django oscar
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'proj1.urls'



AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        'URL': 'http://127.0.0.1:8000/solr/default',
        'INCLUDE_SPELLING': True,
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.checkout.context_processors.default_currency',
                'apps.checkout.context_processors.openinhttps',
                'base.context_processors.main_menus',
                'base.context_processors.textBookcategories',
                'base.context_processors.educationCategories',
                'base.context_processors.cultureCategories',
            ],
        },
    },
]

WSGI_APPLICATION = 'proj1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'ATOMIC_REQUESTS': True,
    }
    
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'andaal/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL='/andaal/media/'
MEDIA_ROOT=BASE_DIR / 'media'




# LOGGING

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }



# Strip Inetgrations 
# Screte Keys


# Paypal Integrations

# PAYPAL_API_USERNAME = 'test_xxxx.gmail.com'
# PAYPAL_API_PASSWORD = '123456789'
# PAYPAL_API_SIGNATURE = '...'

SHOP_NAME = 'ANDAAL'
OSCAR_HOMEPAGE = "/andaal/"

# CHECKOUT SETTINGS 


OSCAR_REQUIRED_ADDRESS_FIELDS = (
    "first_name",
    # "last_name",
    "line1",
    "line4",
    # "postcode",
    "country",
    "phone_number"
)



# OScar SCA STRIP 
OSCAR_DEFAULT_CURRENCY = 'XAF'
STRIPE_CURRENCY= 'xaf'
PAYPAL_CURRENCY = 'EUR'

EXCHANGE_RATE_API_KEY = '482ad3a3cd25e4859b55acec3b2d25d5'
SMS_AUTH_SCRETE_KEY = 'OU54bWFBczdYNUVoVDZCdktBeTlrTWpmOW9tblZnc1U6TnA2V1pjODJLc0VGRkRJcw=='
SMS_SENDER_PHONE_NUMBER = '2473568273'

STRIPE_SEND_RECEIPT =  True
STRIPE_PUBLISHABLE_KEY= "pk_test_TYooMQauvdEDq54NiTphI7jx"
STRIPE_SECRET_KEY= "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
STRIPE_RETURN_URL_BASE= 'http://127.0.0.1:8000/andaal/checkout/preview/'
STRIPE_PAYMENT_SUCCESS_URL = "http://127.0.0.1:8000/andaal/checkout/preview-stripe/{}"
STRIPE_PAYMENT_CANCEL_URL = "http://127.0.0.1:8000/andaal/basket/"


EMAIL_BACKEND ="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "ayaaninam555@gmail.com"
EMAIL_HOST_PASSWORD = "dnqt uzes xapa ntow"


ARE_YOU_USING_ENV = False

# PAYPAL INTEGRATION 

PAYPAL_API_USERNAME = 'sb-qyyzi29402195_api1.business.example.com'
PAYPAL_API_PASSWORD = '9A77LPJLB868MG52'
PAYPAL_API_SIGNATURE = 'Ajzmr6eFvj3JSg2kZotkvdqdQbl8A9js1kfXGFUd4clbiVXvyxi3hzFq'



# PAYPAL SETTING
PAYPAL_CALLBACK_HTTPS = False
# FLUTTER WAVE DETAILS


FLUTTER_WAVE_PUBLIC_KEY = 'FLWPUBK_TEST-7498a1d1740cc05bb7a058307f84eccf-X'
FLUTTER_WAVE_SCRETE_KEY = 'FLWSECK_TEST-11edaca82157cdfe31791a7a663ad54c-X'
FLUTTER_WAVE_ENCRYPTION_KEY = 'FLWSECK_TEST5908b115537e'
FLUTTER_PAYMENT_URL = 'https://api.flutterwave.com/v3/charges?type=mobile_money_franco'

LOGIN_URL = '/andaal/accounts/login/'
LOGIN_REDIRECT_URL = '/andaal/after-registration'




CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TIMEZONE = 'Asia/Karachi'