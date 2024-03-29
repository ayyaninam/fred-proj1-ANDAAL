
from pathlib import Path
import os
from dotenv import load_dotenv
from oscar.defaults import *

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True


if DEBUG:
    dotenv_path = '.env_dev'
else:
    dotenv_path = '.env_prod'

load_dotenv(dotenv_path)

def getenv(name):
    return os.environ.get(name)

SECRET_KEY = getenv('SECRET_KEY')


ALLOWED_HOSTS = []




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
    'apps.communication.apps.CommunicationConfig',
    # End Changed

    'oscar.apps.address.apps.AddressConfig',
    'apps.shipping.apps.ShippingConfig',
    'apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
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
        'DIRS': [os.path.join(BASE_DIR, getenv('TEMPLATE_FOLDER'))],
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
                'base.context_processors.footerdetails',
                'base.context_processors.homepage_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'proj1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': getenv('DB_ENGINE'),
        'NAME': BASE_DIR / getenv('DB_NAME'),
        'ATOMIC_REQUESTS': getenv('DB_ATOMIC_REQUESTS') == 'True',
    }
    
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = getenv('STATIC_URL')
STATIC_ROOT = os.path.join(BASE_DIR, getenv('STATIC_ROOT'))
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL=getenv('MEDIA_URL')
MEDIA_ROOT=BASE_DIR / getenv('MEDIA_ROOT')




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

SHOP_NAME = getenv('SHOP_NAME')
OSCAR_HOMEPAGE = getenv('OSCAR_HOMEPAGE')
OSCAR_SHOP_NAME = getenv('OSCAR_SHOP_NAME')
OSCAR_SHOP_TAGLINE = getenv('OSCAR_SHOP_TAGLINE')

# CHECKOUT SETTINGS 


OSCAR_REQUIRED_ADDRESS_FIELDS = tuple(getenv('OSCAR_REQUIRED_ADDRESS_FIELDS').split(','))



# OScar SCA STRIP 
OSCAR_DEFAULT_CURRENCY = getenv('OSCAR_DEFAULT_CURRENCY')
STRIPE_CURRENCY= getenv('STRIPE_CURRENCY')
PAYPAL_CURRENCY = getenv('PAYPAL_CURRENCY')

EXCHANGE_RATE_API_KEY = getenv('EXCHANGE_RATE_API_KEY')
SMS_AUTH_SCRETE_KEY = getenv('SMS_AUTH_SCRETE_KEY')
SMS_SENDER_PHONE_NUMBER = getenv('SMS_SENDER_PHONE_NUMBER')

STRIPE_SEND_RECEIPT =  getenv('STRIPE_SEND_RECEIPT') == True
STRIPE_PUBLISHABLE_KEY= getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY= getenv('STRIPE_SECRET_KEY')
STRIPE_RETURN_URL_BASE= getenv('STRIPE_RETURN_URL_BASE')
STRIPE_PAYMENT_SUCCESS_URL = getenv('STRIPE_PAYMENT_SUCCESS_URL')
STRIPE_PAYMENT_CANCEL_URL = getenv('STRIPE_PAYMENT_CANCEL_URL')


EMAIL_BACKEND =getenv('EMAIL_BACKEND')
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_USE_TLS = getenv('EMAIL_USE_TLS') == 'True'
EMAIL_PORT = int(getenv('EMAIL_PORT'))
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')


ARE_YOU_USING_ENV = getenv('ARE_YOU_USING_ENV') == 'True'

# PAYPAL INTEGRATION 

PAYPAL_API_USERNAME = getenv('PAYPAL_API_USERNAME')
PAYPAL_API_PASSWORD = getenv('PAYPAL_API_PASSWORD')
PAYPAL_API_SIGNATURE = getenv('PAYPAL_API_SIGNATURE')



# PAYPAL SETTING
PAYPAL_CALLBACK_HTTPS = getenv('PAYPAL_CALLBACK_HTTPS') == 'True'
# FLUTTER WAVE DETAILS


FLUTTER_WAVE_PUBLIC_KEY = getenv('FLUTTER_WAVE_PUBLIC_KEY')
FLUTTER_WAVE_SCRETE_KEY = getenv('FLUTTER_WAVE_SCRETE_KEY')
FLUTTER_WAVE_ENCRYPTION_KEY = getenv('FLUTTER_WAVE_ENCRYPTION_KEY')
FLUTTER_PAYMENT_URL = getenv('FLUTTER_PAYMENT_URL')

LOGIN_URL = getenv('LOGIN_URL')
LOGIN_REDIRECT_URL = getenv('LOGIN_REDIRECT_URL')

# OSCAR_CURRENCY_FORMAT = {
#     'ZAR': {
#         'format': u'R #,##',
#     }
# }
REFRESH_XAF_RATE_AFTER_SEC = int(getenv('REFRESH_XAF_RATE_AFTER_SEC'))

OSCAR_CURRENCY_FORMAT = {
    'XAF': {
        'format': u'FCFA #,###',
    },
    # Add other currency formats if needed
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, 'cache'),
    }
}