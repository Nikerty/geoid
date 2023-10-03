from django.contrib import admin
from .models import *


class GeneralUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'is_active', 'is_ban']
    list_filter = ['is_ban']
    list_display_links = ['user']


class SubUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'is_active', 'is_ban', 'subscription', 'is_sub']
    list_filter = ['is_ban', 'is_sub', 'start_time_sub', 'end_time_sub']
    list_display_links = ['user']


class EditImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user_general', 'user_sub', 'is_done']
    list_filter = ['user_general', 'user_sub', 'is_done']



admin.site.register(GeneralUser, GeneralUserAdmin)
admin.site.register(SubUser, SubUserAdmin)
admin.site.register(EditImage, EditImageAdmin)
admin.site.register(CategoriesNews)
admin.site.register(News)
admin.site.register(TestModel)
# Register your models here.
