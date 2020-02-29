from rest_framework import serializers

from bookings.models import ReservationType, StayType, Reservor, StayReservation, FoodReservation


class ReservationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationType
        fields = '__all__'


class StayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StayType
        fields = '__all__'


class ReservorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservor
        fields = '__all__'


class StayReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StayReservation
        fields = '__all__'


class FoodReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReservation
        fields = '__all__'

