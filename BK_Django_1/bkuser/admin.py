# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Bkuser

from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    
admin.site.register(Bkuser, UserAdmin)