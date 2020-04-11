from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from bookings.models import FoodReservation, StayReservation
from bookings.serializers import FoodReservationSerializer, StayReservationSerializer
from transactions.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
