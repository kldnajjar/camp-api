# Generated by Django 3.0.3 on 2020-03-07 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_company_archived'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stayreservation',
            options={'ordering': ['-reserved_from', '-created_at']},
        ),
    ]