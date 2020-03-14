from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from bookings.filters import CompanyFilter, StayTypeFilter, StayReservationFilter, FoodReservationFilter
from bookings.models import FoodReservation, StayReservation, StayType, Company
from bookings.serializers import FoodReservationSerializer, \
    StayReservationSerializer, CompanySerializer, StayTypeSerializer
from utils.filters import CaseInsensitiveOrderingFilter
from utils.viewsets import ArchivableMixin


class StayTypeModelViewSet(ModelViewSet):
    queryset = StayType.objects.all()
    serializer_class = StayTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = StayTypeFilter
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    ordering_fields = '__all__'


class CompanyModelViewSet(ArchivableMixin, ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = CompanyFilter
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    ordering_fields = '__all__'


class StayReservationModelViewSet(ModelViewSet):
    queryset = StayReservation.objects.all()
    serializer_class = StayReservationSerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = StayReservationFilter
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    ordering_fields = '__all__'
    ordering = ['-reserved_to']


class FoodReservationModelViewSet(ModelViewSet):
    queryset = FoodReservation.objects.all()
    serializer_class = FoodReservationSerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = FoodReservationFilter
    filter_backends = [DjangoFilterBackend, CaseInsensitiveOrderingFilter]
    ordering_fields = '__all__'
    ordering = ['-reservation_date']
