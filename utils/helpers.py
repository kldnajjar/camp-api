from datetime import datetime


def date_in_the_past(d):
    d = datetime(*d.timetuple()[:6]).date()
    return datetime.utcnow().date() > d


def create_permissions_in_migrations():
    from django.apps import apps
    from django.contrib.auth.management import create_permissions

    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None
