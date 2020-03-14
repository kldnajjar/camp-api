from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from bookings.models import FoodReservation, StayReservation
from bookings.serializers import FoodReservationSerializer, StayReservationSerializer
from transactions.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    food_reservation = FoodReservationSerializer(many=False, read_only=True,)
    food_reservation_id = serializers.PrimaryKeyRelatedField(
        source='food_reservation',
        many=False,
        write_only=True,
        queryset=FoodReservation.objects.all(),
        error_messages={
            "does_not_exist": _("Chosen reservation is inavlid.")
        }
    )
    stay_reservation = StayReservationSerializer(many=False, read_only=True)
    stay_reservation_id = serializers.PrimaryKeyRelatedField(
        source="stay_reservation",
        queryset=StayReservation.objects.all(),
        write_only=True,
        many=False,
        error_messages={
            "does_not_exist": _("Chosen reservation is inavlid.")
        }
    )

    class Meta:
        model = Payment
        fields = '__all__'
