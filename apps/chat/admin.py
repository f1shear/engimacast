from django.contrib import admin

# Register your models here.
from .models import ChatRoomModel


@admin.register(ChatRoomModel)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at', )
