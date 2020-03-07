from rest_framework.mixins import DestroyModelMixin


class ArchivableMixin(DestroyModelMixin):
    def perform_destroy(self, instance):
        instance.archived = True
        instance.save()


class ModifiedQuerysetMixin:
    def get_queryset(self):
        # Getting Queryset from Super Viewset Classes
        queryset = super().get_queryset()
        # Modifying the Queryset with this method
        queryset = self.get_modified_queryset(queryset)
        # Return the user related queryset
        return queryset

    # noinspection PyMethodMayBeStatic
    def get_modified_queryset(self, queryset):
        return queryset


def ExcludeHttpMethodsMixin(*args):
    lowercased_args = list(map(lambda m: m.lower(), args))
    methods = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    methods = [method for method in methods if method not in lowercased_args]

    class ExcludedHTTPMethodMixin:
        http_method_names = methods
    return ExcludedHTTPMethodMixin
