from django.contrib import admin

from . import models


@admin.register(models.UserScripts)
class UserScriptsAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active')
    list_editable = 'active',
