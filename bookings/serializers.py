from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bookings.models import StayType, StayReservation, FoodReservation, Company, Reservation
from camp.models import Tent, Activity, MealType, Food
from camp.serializers import TentSerializer, FoodSerializer, ActivitySerializer
from utils.helpers import date_in_the_past


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
        queryset=Tent.objects.all()
    )
    tent = TentSerializer(
        many=False,
        read_only=True,
    )
    activities_ids = serializers.PrimaryKeyRelatedField(
        source='activities',
        many=True,
        required=False,
        queryset=Activity.objects.all()
    )
    activities = ActivitySerializer(
        many=True,
        read_only=True
    )
    price = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        min_value=1,
        required=False
    )
    company = CompanySerializer(
        many=False,
        read_only=True
    )
    company_id = serializers.PrimaryKeyRelatedField(
        source='company',
        queryset=Company.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    stay_type_id = serializers.PrimaryKeyRelatedField(
        source='stay_type',
        queryset=StayType.objects.all()
    )
    stay_type = serializers.CharField(
        source='stay_type.name',
        read_only=True
    )
    reservation_type = serializers.ChoiceField(
        choices=Reservation.TYPE.choices
    )

    def create(self, validated_data):
        tent = validated_data['tent']
        guests_count = validated_data['guests_count']
        date_from = validated_data['reserved_from']
        date_to = validated_data['reserved_to']
        res_type = validated_data['reservation_type']
        company = validated_data.get('company', None)
        company_id = company.id if company else None
        res_number = validated_data.get('reservation_number', None)
        self._check_tent_capacity(tent, guests_count)
        self._check_reservation_dates_are_not_in_the_past(date_from, date_to)
        self._reservation_dates_are_not_valid(date_from, date_to)
        self._tent_is_reserved_in_date_range(tent, date_from, date_to)
        self._check_reservation_number_if_company(res_type, company_id, res_number)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        tent = validated_data.get('tent', None) or instance.tent
        guests_count = validated_data.get('guests_count', None) or instance.guests_count
        date_from = validated_data.get('reserved_from', None)
        date_to = validated_data.get('reserved_to', None)
        res_type = validated_data.get('reservation_type', None) or instance.reservation_type
        company = validated_data.get('company', None) or instance.company
        company_id = company.id if company else None
        res_number = validated_data.get('reservation_number', None) or instance.reservation_number

        self._check_tent_capacity(tent, guests_count)
        if (date_from or date_to) and tent:
            date_from = instance.reserved_from if not date_from else date_from
            date_to = instance.reserved_to if not date_to else date_to
            self._check_reservation_dates_are_not_in_the_past(date_from, date_to)
            self._reservation_dates_are_not_valid(date_from, date_to)
            self._tent_is_reserved_in_date_range(tent, date_from, date_to, instance.id)
        if res_type == Reservation.TYPE.individual and company:
            validated_data['company'] = None
            validated_data['reservation_number'] = None
        self._check_reservation_number_if_company(res_type, company_id, res_number)
        return super().update(instance, validated_data)

    def _check_tent_capacity(self, tent, guests_count):
        if tent.capacity < guests_count:
            raise ValidationError({
                'guests_count': _("Guests count exceeds tent's capacity.")
            })

    def _reservation_dates_are_not_valid(self, date_from, date_to):
        if date_to < date_from:
            raise ValidationError({
                'reserved_to': _("Reserved to date can't be before reserved from date.")
            })

    def _check_reservation_dates_are_not_in_the_past(self, date_from, date_to):
        validation = {}
        if date_in_the_past(date_from):
            validation['reserved_from'] = _('The date you are reserving from can\'t be in the past.')
        if date_in_the_past(date_to):
            validation['reserved_to'] = _('The date you are reserving to can\'t be in the past.')
        if validation:
            raise ValidationError(validation)

    def _check_reservation_number_if_company(self, res_type, company_id, reservation_number):
        validation = {}
        if res_type == Reservation.TYPE.company and not reservation_number:
            validation['reservation_number'] = _("Company reservation can't be done without a reservation number.")
        if res_type == Reservation.TYPE.company and not company_id:
            validation['company_id'] = _("Company reservation can't be done without a company.")
        if validation:
            raise ValidationError(validation)

    def _tent_is_reserved_in_date_range(self, tent, date_from, date_to, exclude_reservation_id=None):
        is_reserved = self.Meta.model.objects.filter(tent=tent).exclude(
            Q(status=[StayReservation.STATUS.cancelled]) |
            Q(reserved_from__gte=date_to) |
            Q(reserved_to__lte=date_from) |
            Q(pk=exclude_reservation_id)
        ).exists()
        if is_reserved:
            raise ValidationError({
                'tent_id': _("Tent is reserved in the specified date range.")
            })

    class Meta:
        model = StayReservation
        fields = '__all__'


# noinspection PyMethodMayBeStatic
class FoodReservationSerializer(serializers.ModelSerializer):
    company = CompanySerializer(
        many=False,
        read_only=True
    )
    company_id = serializers.PrimaryKeyRelatedField(
        source='company',
        queryset=Company.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    price = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        min_value=1,
        required=False
    )
    reservation_type = serializers.ChoiceField(
        choices=Reservation.TYPE.choices
    )
    meal_type = serializers.CharField(
        source='meal_type.name',
        read_only=True
    )
    meal_type_id = serializers.PrimaryKeyRelatedField(
        source='meal_type',
        queryset=MealType.objects.all(),
    )
    food_ids = serializers.PrimaryKeyRelatedField(
        source='food',
        many=True,
        queryset=Food.objects.all()
    )
    food = FoodSerializer(
        many=True,
        read_only=True
    )

    def create(self, validated_data):
        reservation_date = validated_data['reservation_date']
        res_type = validated_data['reservation_type']
        res_number = validated_data.get('reservation_number', None)
        company = validated_data.get('company', None)
        company_id = company.id if company else None
        if res_type == Reservation.TYPE.individual:
            validated_data['company'] = None
            validated_data['reservation_number'] = None
        self._check_reservation_date_not_in_the_past(reservation_date)
        self._check_reservation_number_if_company(res_type, company_id, res_number)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        reservation_date = validated_data.get('reservation_date', None)
        res_type = validated_data.get('reservation_type', None) or instance.reservation_type
        res_number = validated_data.get('reservation_number', None)
        company = validated_data.get('company', None) or instance.company
        company_id = company.id if company else None
        if reservation_date:
            self._check_reservation_date_not_in_the_past(reservation_date)
        if res_type == Reservation.TYPE.individual and company:
            validated_data['company'] = None
            validated_data['reservation_number'] = None
        self._check_reservation_number_if_company(res_type, company_id, res_number)
        return super().update(instance, validated_data)

    def _check_reservation_date_not_in_the_past(self, date_from):
        validation = {}
        if date_in_the_past(date_from):
            validation['reservation_date'] = _('Reservation date can\'t be in the past.')
        if validation:
            raise ValidationError(validation)

    def _check_reservation_number_if_company(self, res_type, company_id, reservation_number):
        validation = {}
        if res_type == Reservation.TYPE.company and not reservation_number:
            validation['reservation_number'] = _("Company reservation can't be done without a reservation number.")
        if res_type == Reservation.TYPE.company and not company_id:
            validation['company_id'] = _("Company reservation can't be done without a company.")
        if validation:
            raise ValidationError(validation)

    class Meta:
        model = FoodReservation
        fields = '__all__'
