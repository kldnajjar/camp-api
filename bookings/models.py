from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_utils.choices import Choices, Choice

from camp.models import TentType, Activity, Food, MealType, Tent
from utils.models import TypesBase


class ReservationType(TypesBase):
    pass


class StayType(TypesBase):
    pass


class Reservor(models.Model):
    class TYPE(Choices):
        individual = Choice('individual', _('Individual'))
        company = Choice('company', _('Company'))

    name = models.CharField(max_length=128)
    number = models.CharField(max_length=20)
    file_number = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    type = models.CharField(
        choices=TYPE.choices,
        default=TYPE.individual,
        max_length=128
    )
    email = models.EmailField(unique=True)


class Reservation(models.Model):
    class STATUS(Choices):
        booked = Choice('booked', _('Booked'))
        confirmed = Choice('confirmed', _('Confirmed'))
        cancelled = Choice('cancelled', _('Cancelled'))
    reserved_by = models.ForeignKey(
        Reservor,
        on_delete=models.SET_NULL,
        null=True
    )
    reservation_type = models.ForeignKey(ReservationType, on_delete=models.PROTECT)
    status = models.CharField(
        choices=STATUS.choices,
        max_length=50,
        default=STATUS.booked
    )
    guests_count = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                1,
                message=_("Minimum number of guests is 1.")
            )
        ]
    )
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StayReservation(Reservation):
    tent = models.ForeignKey(
        Tent,
        on_delete=models.SET_NULL,
        null=True
    )
    stay_type = models.ForeignKey(
        StayType,
        on_delete=models.PROTECT
    )
    reserved_from = models.DateField()
    reserved_to = models.DateField()
    activities = models.ManyToManyField(
        Activity,
        related_query_name='reservations'
    )


class FoodReservation(Reservation):
    meal_type = models.ForeignKey(MealType, on_delete=models.PROTECT)
    food = models.ManyToManyField(
        Food,
        related_query_name='reservations'
    )
