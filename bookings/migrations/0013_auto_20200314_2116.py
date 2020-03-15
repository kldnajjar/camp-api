# Generated by Django 3.0.3 on 2020-03-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_auto_20200314_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodreservation',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='foodreservation',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='foodreservation',
            name='contact_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='stayreservation',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='stayreservation',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stayreservation',
            name='contact_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
