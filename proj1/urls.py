from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.views.static import serve
from django.urls import re_path
import logging

logger = logging.getLogger(__name__)

logger.debug('Debug message')    



urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    # path('^checkout/paypal/', include('paypal.express.urls')),
    path('checkout/paypal/', include('paypal.express.urls')),
]

urlpatterns += i18n_patterns(
    path(_('andaal/admin/'), admin.site.urls),
    path('andaal/', include('base.urls'), name='base'),
    path('andaal/', include(apps.get_app_config('oscar').urls[0])),
    re_path(r'^andaal/media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^andaal/static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)