from django_filters import rest_framework as filters

from bookings.models import Company, StayType


class CompanyFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'contains')

    class Meta:
        model = Company
        fields = ['name', 'email', 'phone_number']


class StayTypeFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'contains')

    class Meta:
        model = StayType
        fields = ['name', 'archived']
