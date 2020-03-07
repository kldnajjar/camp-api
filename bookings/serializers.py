from rest_framework import serializers

from bookings.models import StayType, StayReservation, FoodReservation, Company, Reservation
from bookings.validators import StayReservationValidator, FoodReservationValidator
from camp.models import Tent, Activity, MealType, Food
from camp.serializers import TentSerializer


class StayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StayType
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


# noinspection PyMethodMayBeStatic
class StayReservationSerializer(serializers.ModelSerializer):
    tent_id = serializers.PrimaryKeyRelatedField(
        source='tent',
        required=True,
        write_only=True,
        queryset=Tent.objects.all()
    )
    tent = TentSerializer(
        many=False,
        read_only=True,
    )
    activities_ids = serializers.PrimaryKeyRelatedField(
        source='activities',
        many=True,
        write_only=True,
        required=False,
        queryset=Activity.objects.all()
    )
    activities = serializers.SerializerMethodField(
        method_name='get_activities_names',
        read_only=True
    )
    price = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        min_value=1
    )
    company = CompanySerializer(
        many=False,
        read_only=True
    )
    company_id = serializers.PrimaryKeyRelatedField(
        source='company',
        queryset=Company.objects.all(),
        write_only=True,
        required=False
    )
    stay_type_id = serializers.PrimaryKeyRelatedField(
        source='stay_type',
        write_only=True,
        queryset=StayType.objects.all()
    )
    stay_type = serializers.CharField(
        source='stay_type.name',
        read_only=True
    )
    reservation_type = serializers.ChoiceField(
        choices=Reservation.TYPE.choices
    )

    def get_activities_names(self, instance):
        return instance.activities.values_list('name', flat=True)

    class Meta:
        model = StayReservation
        fields = '__all__'
        validators = [
            StayReservationValidator(
                queryset=StayReservation.objects.all()
            )
        ]


# noinspection PyMethodMayBeStatic
class FoodReservationSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        min_value=1
    )
    reservation_type = serializers.CharField()
    meal_type = serializers.CharField(
        source='meal_type.name',
        read_only=True
    )
    meal_type_id = serializers.PrimaryKeyRelatedField(
        source='meal_type',
        queryset=MealType.objects.all(),
        write_only=True
    )
    food_ids = serializers.PrimaryKeyRelatedField(
        source='food',
        many=True,
        write_only=True,
        queryset=Food.objects.all()
    )
    food = serializers.SerializerMethodField(
        'get_food_names',
        read_only=True
    )

    def get_food_names(self, instance):
        return instance.food.values_list('name', flat=True)

    class Meta:
        model = FoodReservation
        validators = [
            FoodReservationValidator()
        ]
        fields = '__all__'
