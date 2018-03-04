from django.contrib import admin

# Register your models here.
from .models import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name',
                    'last_name', 'email', 'is_active', 'is_superuser',
                    'is_staff', 'last_login',)
