import django_filters

from .models import ChatRoomModel


class ChatRoomFilter(django_filters.FilterSet):
    class Meta:
        model = ChatRoomModel
        fields = {
            'name': ['exact', 'icontains', ],
        }
