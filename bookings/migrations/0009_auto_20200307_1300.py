# Generated by Django 3.0.3 on 2020-03-07 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_auto_20200307_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='phone',
            new_name='phone_number',
        ),
    ]