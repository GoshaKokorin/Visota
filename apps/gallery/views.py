from django.shortcuts import render
from apps.gallery.models import Gallery
from django.http import HttpResponseRedirect


def gallery(request):
    context = {}

    photos = Gallery.objects.all()
    context['photos'] = photos

    return render(request, 'gallery.html', context)