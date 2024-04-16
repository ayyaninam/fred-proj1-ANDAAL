
from pathlib import Path
import os
from dotenv import load_dotenv
from oscar.defaults import *
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False


if DEBUG:
    # dotenv_path = '.env_prod'
    dotenv_path = '.env_dev'
else:
    dotenv_path = '.env_prod'

load_dotenv(dotenv_path)


SECRET_KEY = os.environ.get('SECRET_KEY')


ALLOWED_HOSTS = ['*']




INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'oscar_stripe_sca',
    'modeltranslation',

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
    'rosetta',
    # 'parler',
] 

SITE_ID = 1
AUTH_USER_MODEL = "base.User"
ROSETTA_SHOW_AT_ADMIN_PANEL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, os.environ.get('TEMPLATE_FOLDER'))],
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
                'base.context_processors.important_links',
                'base.context_processors.booksCategories',
            ],
        },
    },
]

WSGI_APPLICATION = 'proj1.wsgi.application'


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.path.join(BASE_DIR , os.environ.get('DB_NAME')),
            'ATOMIC_REQUESTS': os.environ.get('DB_ATOMIC_REQUESTS') == 'True',
        }
        
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
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


# Languages Editing 

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_L10N = True

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'fr')



STATIC_URL = os.environ.get('STATIC_URL')
STATIC_ROOT = os.path.join(BASE_DIR, os.environ.get('STATIC_ROOT'))
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL=os.environ.get('MEDIA_URL')

MEDIA_ROOT = os.path.join(BASE_DIR , os.environ.get('MEDIA_ROOT'))




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

SHOP_NAME = os.environ.get('SHOP_NAME')
OSCAR_HOMEPAGE = os.environ.get('OSCAR_HOMEPAGE')
OSCAR_SHOP_NAME = os.environ.get('OSCAR_SHOP_NAME')
OSCAR_SHOP_TAGLINE = os.environ.get('OSCAR_SHOP_TAGLINE')

# CHECKOUT SETTINGS 


OSCAR_REQUIRED_ADDRESS_FIELDS = tuple(os.environ.get('OSCAR_REQUIRED_ADDRESS_FIELDS').split(','))



# OScar SCA STRIP 
OSCAR_DEFAULT_CURRENCY = os.environ.get('OSCAR_DEFAULT_CURRENCY')
STRIPE_CURRENCY= os.environ.get('STRIPE_CURRENCY')
PAYPAL_CURRENCY = os.environ.get('PAYPAL_CURRENCY')

EXCHANGE_RATE_API_KEY = os.environ.get('EXCHANGE_RATE_API_KEY')
SMS_AUTH_SCRETE_KEY = os.environ.get('SMS_AUTH_SCRETE_KEY')
SMS_SENDER_PHONE_NUMBER = os.environ.get('SMS_SENDER_PHONE_NUMBER')

STRIPE_SEND_RECEIPT =  os.environ.get('STRIPE_SEND_RECEIPT') == True
STRIPE_PUBLISHABLE_KEY= os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY= os.environ.get('STRIPE_SECRET_KEY')
STRIPE_RETURN_URL_BASE= os.environ.get('STRIPE_RETURN_URL_BASE')
STRIPE_PAYMENT_SUCCESS_URL = os.environ.get('STRIPE_PAYMENT_SUCCESS_URL')
STRIPE_PAYMENT_CANCEL_URL = os.environ.get('STRIPE_PAYMENT_CANCEL_URL')


EMAIL_BACKEND =os.environ.get('EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS') == 'True'
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


ARE_YOU_USING_ENV = os.environ.get('ARE_YOU_USING_ENV') == 'True'

# PAYPAL INTEGRATION 

PAYPAL_API_USERNAME = os.environ.get('PAYPAL_API_USERNAME')
PAYPAL_API_PASSWORD = os.environ.get('PAYPAL_API_PASSWORD')
PAYPAL_API_SIGNATURE = os.environ.get('PAYPAL_API_SIGNATURE')



# PAYPAL SETTING
PAYPAL_CALLBACK_HTTPS = os.environ.get('PAYPAL_CALLBACK_HTTPS') == 'True'
# FLUTTER WAVE DETAILS


FLUTTER_WAVE_PUBLIC_KEY = os.environ.get('FLUTTER_WAVE_PUBLIC_KEY')
FLUTTER_WAVE_SCRETE_KEY = os.environ.get('FLUTTER_WAVE_SCRETE_KEY')
FLUTTER_WAVE_ENCRYPTION_KEY = os.environ.get('FLUTTER_WAVE_ENCRYPTION_KEY')
FLUTTER_PAYMENT_URL = os.environ.get('FLUTTER_PAYMENT_URL')

LOGIN_URL = os.environ.get('LOGIN_URL')
LOGIN_REDIRECT_URL = os.environ.get('LOGIN_REDIRECT_URL')

# OSCAR_CURRENCY_FORMAT = {
#     'ZAR': {
#         'format': u'R #,##',
#     }
# }
REFRESH_XAF_RATE_AFTER_SEC = int(os.environ.get('REFRESH_XAF_RATE_AFTER_SEC'))

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