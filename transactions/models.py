from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_utils.choices import Choices, Choice

from bookings.models import StayReservation, FoodReservation


class Payment(models.Model):
    class TYPE(Choices):
        cash = Choice('cash', _("Cash"))
        credit = Choice('credit', _("Credit"))

    payment_type = models.CharField(
        max_length=50,
        choices=TYPE.choices
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    expenses = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0
    )
    date = models.DateField()
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
