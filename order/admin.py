from django.contrib import admin
from .models import *


# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Order, ModelAdmin)