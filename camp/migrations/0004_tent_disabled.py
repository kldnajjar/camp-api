# Generated by Django 3.0.3 on 2020-03-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0003_auto_20200307_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='tent',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
