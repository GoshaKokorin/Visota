from django.urls import path
from apps.landing.views import *

urlpatterns = [
    path('', index, name='home'),
    path('master-classes/', master_classes_all, name='master_classes_all'),
    path('master-classes/<str:slug>/', master_classes, name='master_classes'),
    path('master-class/<str:slug>/', master_class_item, name='master_class_item'),
    path('group_lessons/', group_lessons_all, name='group_lessons_all'),
    path('group-lessons/<str:slug>/', group_lessons, name='group_lessons'),
    path('group-lesson/<str:slug>/', group_lessons_item, name='group_lessons_item'),
    path('group-lesson/<str:slug>/', group_lessons_item, name='group_lessons_item'),
    path('blog-list', blog_list, name='blog_list'),
    path('blog-list/<str:slug>/', blog_details, name='blog_details'),

]
