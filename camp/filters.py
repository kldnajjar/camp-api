from django_filters import rest_framework as filters

from camp.models import Tent, Activity, MealType, Food, TentType


class TentTypeFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'contains')

    class Meta:
        model = TentType
        fields = ['id', 'name', 'archived']


class FoodFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'contains')

    class Meta:
        model = Food
        fields = ['id', 'name', 'archived']


class MealTypeFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'contains')

    class Meta:
        model = MealType
        fields = ['id', 'name', 'archived']


class ActivityFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'contains')
    archived = filters.BooleanFilter('archived')

    class Meta:
        model = Activity
        fields = ['id', 'name', 'archived']


class TentFilter(filters.FilterSet):
    name = filters.CharFilter('name', 'contains')
    archived = filters.BooleanFilter('archived')

    class Meta:
        model = Tent
        fields = ['id', 'name', 'archived']

