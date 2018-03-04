import django_filters

from .models import CompanyModel, CompanyEventModel


class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = CompanyModel
        fields = {
            'name': ['exact', 'icontains', ],
            'company_type': ['exact', 'in']
        }


class CompanyEventFilter(django_filters.FilterSet):
    class Meta:
        model = CompanyEventModel
        fields = {
            'company__name': ['icontains', 'exact'],
            'name': ['icontains', 'exact', 'in'],
            'event_type': ['exact', 'in']
        }
