from django.contrib import admin

from .models import CompanyModel, CompanyEventModel


# Register your models here.


@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'company_type', 'description',)


@admin.register(CompanyEventModel)
class CompanyEventAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'event_type', 'start', 'end',)
