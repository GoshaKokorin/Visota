from django.shortcuts import render
from apps.landing.forms import ContactForm
from apps.landing.models import *
from django.http import HttpResponseRedirect, Http404


def index(request):
    context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('')

    context['form'] = ContactForm()

    context['blog'] = BlogDetails.objects.order_by("-id")

    context['master_classes'] = MasterClass.objects.all()
    context['group_lessons'] = GroupLessons.objects.all()

    if VideoIndex.objects.exists():
        video = VideoIndex.objects.first()
        context['video'] = video

    if GroupLessonsItem.objects.filter(slug='podgotovka-k-shkole').exists():
        prodl = GroupLessonsItem.objects.get(slug='podgotovka-k-shkole')
        context['prodl'] = prodl

    if GroupLessonsItem.objects.filter(slug='podgotovka-k-shkole').exists():
        prodl = GroupLessonsItem.objects.get(slug='podgotovka-k-shkole')
        context['prodl'] = prodl

    return render(request, 'index.html', context)


def master_classes_all(request):
    context = {}

    item = MasterClassItem.objects.filter(publish=True)
    context['master_class_item'] = item

    return render(request, 'master_classes.html', context)


def master_classes(request, slug):
    context = {}

    master_class = MasterClass.objects.get(slug=slug)
    context['master_class'] = master_class
    context['master_class_item'] = master_class.master_class_item.filter(publish=True)

    return render(request, 'master_classes.html', context)


def master_class_item(request, slug):
    context = {}

    master_class_item = MasterClassItem.objects.get(slug=slug)
    context['master_class_item'] = master_class_item

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('')

    context['form'] = ContactForm()

    return render(request, 'master_class_item.html', context)


# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------


def group_lessons_all(request):
    context = {}

    context['group_lessons_item'] = GroupLessonsItem.objects.all()

    return render(request, 'group_lessons.html', context)


def group_lessons(request, slug):
    context = {}

    group_lessons = GroupLessons.objects.get(slug=slug)
    context['group_lessons'] = group_lessons
    context['group_lessons_item'] = group_lessons.group_lessons_item.all()

    return render(request, 'group_lessons.html', context)


def group_lessons_item(request, slug):
    context = {}

    group_lesson_item = GroupLessonsItem.objects.get(slug=slug)
    context['group_lesson_item'] = group_lesson_item

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('')

    context['form'] = ContactForm()

    return render(request, 'group_lessons_item.html', context)


def blog_list(request):
    context = {}

    context['blog'] = BlogDetails.objects.all()

    return render(request, 'blog_list.html', context)


def blog_details(request, slug):
    context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/blog-list')

    context['form'] = ContactForm()

    blog = BlogDetails.objects.get(slug=slug)
    context['blog'] = blog

    return render(request, 'blog_details.html', context)
