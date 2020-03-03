from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError

from bookings.models import StayReservation
from utils.helpers import date_in_the_past


# Serializer Validators
# noinspection PyMethodMayBeStatic
class StayReservationValidator:
    def __init__(self, queryset):
        self.queryset = queryset

    def __call__(self, value, *args, **kwargs):
        tent = value['tent']
        date_from = value['reserved_from']
        date_to = value['reserved_to']
        res_type = value['reservation_type']
        res_number = value.get('reservation_number', None)
        self._check_tent_capacity(tent, value['guests_count'])
        self._check_reservation_dates_are_not_in_the_past(date_from, date_to)
        self._reservation_dates_are_not_valid(date_from, date_to)
        self._tent_is_reserved_in_date_range(tent, date_from, date_to)
        self._check_reservation_number_if_company(res_type, res_number)

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

    def _tent_is_reserved_in_date_range(self, tent, date_from, date_to):
        is_reserved = self.queryset.filter(tent=tent).exclude(
            Q(status=[StayReservation.STATUS.cancelled]) |
            Q(reserved_from__gte=date_to) |
            Q(reserved_to__lte=date_from)
        ).exists()
        if is_reserved:
            raise ValidationError({
                'tent': _("Tent is reserved in the specified date range.")
            })

    def _check_reservation_number_if_company(self, res_type, reservation_number):
        if res_type.name == 'Company' and not reservation_number:
            raise ValidationError({
                'reservation_number': _("Company reservation can't be done without a reservation number.")
            })


# noinspection PyMethodMayBeStatic
class FoodReservationValidator:
    def __init__(self):
        pass

    def __call__(self, value, *args, **kwargs):
        reservation_date = value['reservation_date']
        res_type = value['reservation_type']
        res_number = value.get('reservation_number', None)
        self._check_reservation_dates_are_not_in_the_past(reservation_date)
        self._check_reservation_number_if_company(res_type, res_number)

    def _check_reservation_dates_are_not_in_the_past(self, date_from):
        validation = {}
        if date_in_the_past(date_from):
            validation['reservation_date'] = _('Reservation date can\'t be in the past.')
        if validation:
            raise ValidationError(validation)

    def _check_reservation_number_if_company(self, res_type, reservation_number):
        if res_type.name == 'Company' and not reservation_number:
            raise ValidationError({
                'reservation_number': _("Company reservation can't be done without a reservation number.")
            })

# Model Validators
