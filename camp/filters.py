from django_filters import rest_framework as filters

from camp.models import Tent, Activity, MealType, Food, TentType
from utils.filters import FilterDefaultValuesMixin


class TentTypeFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'archived': False}
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = TentType
        fields = ['id', 'name', 'archived', 'disabled']


class FoodFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'archived': False}
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = Food
        fields = ['id', 'name', 'archived', 'disabled']


class MealTypeFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'archived': False}
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = MealType
        fields = ['id', 'name', 'archived', 'disabled']


class ActivityFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'archived': False}
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = Activity
        fields = ['id', 'name', 'archived', 'disabled']


class TentFilter(FilterDefaultValuesMixin, filters.FilterSet):
    defaults = {'archived': False}
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = Tent
        fields = ['id', 'name', 'archived']

