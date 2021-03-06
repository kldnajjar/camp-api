from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from camp.filters import TentFilter, TentTypeFilter, FoodFilter, MealTypeFilter, ActivityFilter
from camp.models import Food, MealType, Activity, Tent, TentType
from camp.serializers import TentSerializer, FoodSerializer, \
    MealTypeSerializer, ActivitySerializer, TentTypeSerializer
from utils.filters import CaseInsensitiveOrderingFilter
from utils.viewsets import ArchivableMixin


class TentTypeModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = TentTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = TentType.objects.all()
    filterset_class = TentTypeFilter
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    ordering_fields = '__all__'


class FoodModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = FoodSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Food.objects.all()
    filterset_class = FoodFilter
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    ordering_fields = '__all__'


class MealTypeModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = MealTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    queryset = MealType.objects.all()
    filterset_class = MealTypeFilter
    ordering_fields = '__all__'


class ActivityModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Activity.objects.all()
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    filterset_class = ActivityFilter
    ordering_fields = '__all__'


class TentModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = TentSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Tent.objects.all()
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    filterset_class = TentFilter
    ordering_fields = '__all__'

# TODO
# 8. Daily Cash (90%) -- Payment data aggregation left for daily cash page.
# 9. Booking.com integration (HUGE and IMPORTANT).
