from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_utils.choices import Choices, Choice

from camp.models import Activity, Food, MealType, Tent
from utils.models import TypesBase


class StayType(TypesBase):
    pass


class Company(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    email = models.EmailField(unique=True)


class Reservation(models.Model):
    class STATUS(Choices):
        booked = Choice('booked', _('Booked'))
        confirmed = Choice('confirmed', _('Confirmed'))
        cancelled = Choice('cancelled', _('Cancelled'))

    class TYPE(Choices):
        individual = Choice('individual', _("Individual"))
        company = Choice('company', _("Company"))

    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=128)
    contact_email = models.EmailField()
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True
    )
    reservation_type = models.CharField(
        max_length=50,
        choices=TYPE.choices,
        default=TYPE.individual
    )
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
    notes = models.TextField(null=True, blank=True)
    reservation_number = models.CharField(max_length=50, null=True, blank=True)
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
    reservation_date = models.DateField()
