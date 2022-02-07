from django.contrib import admin
from .models import *
from tinymce.widgets import AdminTinyMCE
from django.db.models.fields import TextField


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(MasterClass)
class MasterClassAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


class MasterClassPrice(admin.TabularInline):
    model = MasterClassPrice
    extra = 0


class MasterClassPoint(admin.TabularInline):
    model = MasterClassPoint
    extra = 0


@admin.register(MasterClassItem)
class MasterClassItemAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [MasterClassPoint, MasterClassPrice]

    formfield_overrides = {
        TextField: {'widget': AdminTinyMCE(attrs={'cols': 40, 'rows': 30}, )},
    }

    # ----------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------


@admin.register(GroupLessons)
class GroupLessonsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


class GroupLessonsPrice(admin.TabularInline):
    model = GroupLessonsPrice
    extra = 0


class GroupLessonsPoint(admin.TabularInline):
    model = GroupLessonsPoint
    extra = 0


@admin.register(GroupLessonsItem)
class GroupLessonsItemAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GroupLessonsPoint, GroupLessonsPrice]

    formfield_overrides = {
        TextField: {'widget': AdminTinyMCE(attrs={'cols': 40, 'rows': 30}, )},
    }


@admin.register(VideoIndex)
class VideoIndexAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(BlogDetails)
class BlogDetailsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

    formfield_overrides = {
        TextField: {'widget': AdminTinyMCE(attrs={'cols': 40, 'rows': 30}, )},
    }