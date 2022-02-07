from django.urls import path
from apps.gallery.views import gallery

urlpatterns = [
    path('', gallery, name='gallery'),
]