from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from bookings.models import FoodReservation, StayReservation, Reservor, \
    StayType, ReservationType
from bookings.serializers import FoodReservationSerializer, \
    StayReservationSerializer, ReservorSerializer, StayTypeSerializer, \
    ReservationTypeSerializer


class ReservationTypeModelViewSet(ModelViewSet):
    queryset = ReservationType.objects.all()
    serializer_class = ReservationTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    pagination_class = None


class StayTypeModelViewSet(ModelViewSet):
    queryset = StayType.objects.all()
    serializer_class = StayTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    pagination_class = None


class ReservorModelViewSet(ModelViewSet):
    queryset = Reservor.objects.all()
    serializer_class = ReservorSerializer
    permission_classes = (DjangoModelPermissions,)


class StayReservationModelViewSet(ModelViewSet):
    queryset = StayReservation.objects.all()
    serializer_class = StayReservationSerializer
    permission_classes = (DjangoModelPermissions,)


class FoodReservationModelViewSet(ModelViewSet):
    queryset = FoodReservation.objects.all()
    serializer_class = FoodReservationSerializer
    permission_classes = (DjangoModelPermissions,)
