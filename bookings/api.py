from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from bookings.filters import CompanyFilter, StayTypeFilter, StayReservationFilter, FoodReservationFilter
from bookings.models import FoodReservation, StayReservation, StayType, Company
from bookings.serializers import FoodReservationSerializer, \
    StayReservationSerializer, CompanySerializer, StayTypeSerializer
from utils.viewsets import ArchivableMixin


class StayTypeModelViewSet(ModelViewSet):
    queryset = StayType.objects.all()
    serializer_class = StayTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = StayTypeFilter
    ordering_fields = ['name', 'disabled', 'archived']


class CompanyModelViewSet(ArchivableMixin, ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = CompanyFilter
    ordering_fields = ['name', 'archived']


class StayReservationModelViewSet(ModelViewSet):
    queryset = StayReservation.objects.all()
    serializer_class = StayReservationSerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = StayReservationFilter


class FoodReservationModelViewSet(ModelViewSet):
    queryset = FoodReservation.objects.all()
    serializer_class = FoodReservationSerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = FoodReservationFilter
