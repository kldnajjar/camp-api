import re

from django_filters import rest_framework as filters

from bookings.models import Company, StayType, StayReservation, FoodReservation, Reservation
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


class StayReservationFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'status': ['booked', 'confirmed']}
    document_number = filters.NumberFilter('id')
    reserved_from__gte = filters.DateFilter('reserved_from', 'gte')
    reserved_to__lte = filters.DateFilter('reserved_to', 'lte')
    reservation_number = filters.CharFilter('reservation_number', 'icontains')
    contact_name = filters.CharFilter('contact_name', 'icontains')
    contact_number = filters.CharFilter('contact_number', 'icontains')
    contact_email = filters.CharFilter('contact_email', 'icontains')
    status = filters.MultipleChoiceFilter('status', choices=Reservation.STATUS.choices)
    activities_ids = filters.CharFilter(method='activities_filter')

    def activities_filter(self, queryset, name, value):
        value = re.split(r'\s*,\s*', value) if isinstance(value, str) else value
        return queryset.filter(activities__id__in=value)

    class Meta:
        model = StayReservation
        fields = ['document_number', 'reserved_from', 'reserved_from__gte',
                  'tent_id', 'price', 'reserved_to', 'reserved_to__lte', 'stay_type',
                  'status', 'reservation_number', 'contact_name', 'contact_number',
                  'contact_email', 'company_id', 'guests_count',
                  'created_at', 'reservation_type', 'activities_ids']


class FoodReservationFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'status': ['booked', 'confirmed']}
    document_number = filters.NumberFilter('id')
    reservation_date__lte = filters.DateFilter('reservation_date', 'lte')
    reservation_date__gte = filters.DateFilter('reservation_date', 'gte')
    reservation_number = filters.CharFilter('reservation_number', 'icontains')
    contact_name = filters.CharFilter('contact_name', 'icontains')
    contact_number = filters.CharFilter('contact_number', 'icontains')
    contact_email = filters.CharFilter('contact_email', 'icontains')
    company = filters.CharFilter('company__name', 'icontains')
    status = filters.MultipleChoiceFilter('status', choices=Reservation.STATUS.choices)
    food_ids = filters.CharFilter(method='food_filter')

    def food_filter(self, qs, name, value):
        value = re.split(r'\s*,\s*', value) if isinstance(value, str) else value
        return qs.filter(food__id__in=value)

    class Meta:
        model = FoodReservation
        fields = ['document_number', 'reservation_date', 'reservation_date__gte',
                  'reservation_date__lte', 'status', 'reservation_number',
                  'contact_name', 'contact_number', 'contact_email',
                  'company', 'company_id', 'meal_type_id', 'food_ids',
                  'reservation_type', 'created_at', 'guests_count', 'price']
