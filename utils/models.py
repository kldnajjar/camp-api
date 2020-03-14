from django.db import models


class TypesBase(models.Model):
    name = models.CharField(max_length=100)
    disabled = models.BooleanField(default=False, null=False, blank=False)
    archived = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        abstract = True
