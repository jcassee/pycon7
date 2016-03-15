from django.contrib import admin

from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ['name', 'imo']
