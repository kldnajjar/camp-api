from django.db import models


class TypesBase(models.Model):
    name = models.CharField(max_length=100)
    disabled = models.BooleanField(default=False, null=False)
    archived = models.BooleanField(default=False, null=False)

    class Meta:
        abstract = True
