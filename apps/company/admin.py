from django.contrib import admin

# Register your models here.


from .models import CompanyModel, CompanyEventModel


@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'company_type', 'description', )


@admin.register(CompanyEventModel)
class CompanyEventAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'event_type', 'start', 'end',)
