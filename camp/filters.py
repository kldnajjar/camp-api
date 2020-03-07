from django_filters import rest_framework as filters

from camp.models import Tent, Activity, MealType, Food, TentType


class TentTypeFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = TentType
        fields = ['id', 'name', 'archived', 'disabled']


class FoodFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = Food
        fields = ['id', 'name', 'archived', 'disabled']


class MealTypeFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = MealType
        fields = ['id', 'name', 'archived', 'disabled']


class ActivityFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = Activity
        fields = ['id', 'name', 'archived', 'disabled']


class TentFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'icontains')

    class Meta:
        model = Tent
        fields = ['id', 'name', 'archived']

