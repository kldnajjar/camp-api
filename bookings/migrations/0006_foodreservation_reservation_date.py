# Generated by Django 3.0.3 on 2020-03-03 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20200303_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodreservation',
            name='reservation_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 3, 15, 40, 7, 51449)),
            preserve_default=False,
        ),
    ]