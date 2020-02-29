from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import TypesBase


class TentType(TypesBase):
    pass


class Food(TypesBase):
    pass


class MealType(TypesBase):
    pass


class Activity(TypesBase):
    pass


class Tent(models.Model):
    tent_type = models.ForeignKey(TentType, on_delete=models.PROTECT)
    capacity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, _("Minimum tent capacity is 1."))
        ]
    )
