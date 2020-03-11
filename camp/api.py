from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from camp.filters import TentFilter, TentTypeFilter, FoodFilter, MealTypeFilter, ActivityFilter
from camp.models import Food, MealType, Activity, Tent, TentType
from camp.serializers import TentSerializer, FoodSerializer, \
    MealTypeSerializer, ActivitySerializer, TentTypeSerializer
from utils.viewsets import ArchivableMixin


class TentTypeModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = TentTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = TentType.objects.all()
    filterset_class = TentTypeFilter
    ordering_fields = ['name', 'disabled', 'archived']


class FoodModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = FoodSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Food.objects.all()
    filterset_class = FoodFilter
    ordering_fields = ['name', 'disabled', 'archived']


class MealTypeModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = MealTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = MealType.objects.all()
    filterset_class = MealTypeFilter
    ordering_fields = ['name', 'disabled', 'archived']


class ActivityModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Activity.objects.all()
    filterset_class = ActivityFilter
    ordering_fields = ['name', 'disabled', 'archived']


class TentModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = TentSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Tent.objects.all()
    filterset_class = TentFilter
    ordering_fields = ['name', 'archived']

# TODO
# 5. Ordering for all APIs.
# 8. Daily Cash
# 9. Booking.com integration (HUGE and IMPORTANT).
