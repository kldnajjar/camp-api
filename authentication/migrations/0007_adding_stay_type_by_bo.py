# Generated by Django 3.0.3 on 2020-03-28 15:14

from django.db import migrations

from utils.helpers import create_permissions_in_migrations


def add_delete_stay_type_permission(apps, schema_editor):
    create_permissions_in_migrations()
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    db_alias = schema_editor.connection.alias
    bo_group = Group.objects.using(db_alias).filter(name='business_owner').first()
    bo_group.permissions.add(Permission.objects.get(codename='delete_staytype'))
    bo_group.save()


def remove_delete_sta_type_permission(apps, schema_editor):
    create_permissions_in_migrations()
    Group = apps.get_model('auth', 'Group')
    db_alias = schema_editor.connection.alias
    bo_group = Group.objects.using(db_alias).filter(name='business_owner').first()
    bo_group.permissions.filter(codename='delete_staytype').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_add_payments_permissions'),
    ]

    operations = [
        migrations.RunPython(add_delete_stay_type_permission, remove_delete_sta_type_permission)
    ]
