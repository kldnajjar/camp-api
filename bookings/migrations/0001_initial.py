# Generated by Django 3.0.3 on 2020-02-29 15:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_utils.choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('disabled', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=20)),
                ('file_number', models.CharField(blank=True, max_length=256, null=True)),
                ('type', models.CharField(choices=[('individual', django_utils.choices.Choice('individual', 'Individual')), ('company', django_utils.choices.Choice('company', 'Company'))], default='individual', max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='StayType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('disabled', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StayReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('booked', django_utils.choices.Choice('booked', 'Booked')), ('confirmed', django_utils.choices.Choice('confirmed', 'Confirmed')), ('cancelled', django_utils.choices.Choice('cancelled', 'Cancelled'))], default='booked', max_length=50)),
                ('guests_count', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Minimum number of guests is 1.')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reserved_from', models.DateField()),
                ('reserved_to', models.DateField()),
                ('activities', models.ManyToManyField(related_query_name='reservations', to='camp.Activity')),
                ('reservation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.ReservationType')),
                ('reserved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Reservor')),
                ('stay_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.StayType')),
                ('tent_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='camp.TentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FoodReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('booked', django_utils.choices.Choice('booked', 'Booked')), ('confirmed', django_utils.choices.Choice('confirmed', 'Confirmed')), ('cancelled', django_utils.choices.Choice('cancelled', 'Cancelled'))], default='booked', max_length=50)),
                ('guests_count', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Minimum number of guests is 1.')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('food', models.ManyToManyField(related_query_name='reservations', to='camp.Food')),
                ('meal_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='camp.MealType')),
                ('reservation_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.ReservationType')),
                ('reserved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Reservor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
