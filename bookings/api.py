from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from bookings.models import FoodReservation, StayReservation, StayType, Company
from bookings.serializers import FoodReservationSerializer, \
    StayReservationSerializer, CompanySerializer, StayTypeSerializer


class StayTypeModelViewSet(ModelViewSet):
    queryset = StayType.objects.all()
    serializer_class = StayTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    pagination_class = None


class CompanyModelViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (DjangoModelPermissions,)


class StayReservationModelViewSet(ModelViewSet):
    queryset = StayReservation.objects.all()
    serializer_class = StayReservationSerializer
    permission_classes = (DjangoModelPermissions,)


class FoodReservationModelViewSet(ModelViewSet):
    queryset = FoodReservation.objects.all()
    serializer_class = FoodReservationSerializer
    permission_classes = (DjangoModelPermissions,)
