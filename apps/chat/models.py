from django.db import models

# Create your models here.
from users.models import UserModel


class ChatRoomModel(models.Model):

    created_by = models.ForeignKey(
        UserModel, related_name='+', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_room'
