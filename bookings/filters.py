from django_filters import rest_framework as filters

from bookings.models import Company, StayType, StayReservation
from utils.filters import FilterDefaultValuesMixin


class CompanyFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'archived': False}
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = Company
        fields = ['name', 'email', 'phone_number', 'archived']


class StayTypeFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'archived': False}
    name = filters.CharFilter('name', 'contains')

    class Meta:
        model = StayType
        fields = ['name', 'archived', 'disabled']


class StayReservationFilter(filters.FilterSet):
    reserved_from__gte = filters.DateFilter('reserved_from', 'gte')
    reserved_to__lte = filters.DateFilter('reserved_to', 'lte')
    reservation_number = filters.CharFilter('reservation_number', 'icontains')
    contact_name = filters.CharFilter('contact_name', 'icontains')
    contact_number = filters.CharFilter('contact_number', 'icontains')
    contact_email = filters.CharFilter('contact_email', 'icontains')
    company = filters.CharFilter('company__name', 'icontains')

    class Meta:
        model = StayReservation
        fields = ['reserved_from', 'reserved_from__gte',
                  'reserved_to', 'reserved_to__lte', 'stay_type',
                  'status', 'reservation_number', 'contact_name',
                  'contact_number', 'contact_email', 'company', 'company_id']
