from django.contrib import admin
from django.urls import path, include
from apps.landing.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('gallery/', include('apps.gallery.urls')),
                  path('', include('apps.landing.urls')),
                  path('tinymce/', include('tinymce.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
