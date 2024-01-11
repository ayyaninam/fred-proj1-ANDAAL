from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# New Code
from django.shortcuts import redirect

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    path('', lambda request: redirect('andaal/', permanent=True)),
    path('admin/', admin.site.urls),
    path('andaal/', include('base.urls')),
    path('andaal/', include(apps.get_app_config('oscar').urls[0])),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)