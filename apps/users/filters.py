import django_filters


from .models import UserModel


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = UserModel
        fields = {
            'username': ['exact',],
        }