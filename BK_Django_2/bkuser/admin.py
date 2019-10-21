from django.contrib import admin
from .models import Bkuser

# Register your models here.
class BkuserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Bkuser, BkuserAdmin)