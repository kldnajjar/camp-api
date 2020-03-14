from django.db.models.functions import Lower
from rest_framework.filters import OrderingFilter


class FilterDefaultValuesMixin:
    # Key-Value Dict for setting default values
    defaults = {}

    # Inject Defaults on initialization
    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = self._set_defaults(data.copy())
        super().__init__(data, *args, **kwargs)

    # Sets the default values to the received data.
    def _set_defaults(self, data):
        unset_filters = set(self.base_filters.keys()).difference(set(data.keys()))
        for key in self.defaults.keys():
            if key in unset_filters:
                if isinstance(self.defaults[key], list):
                    data.setlist(key, self.defaults[key])
                else:
                    data[key] = self.defaults[key]
        return data


class CaseInsensitiveOrderingFilter(OrderingFilter):
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)

        if ordering:
            case_insensitive_ordering = []
            for field in ordering:
                case_insensitive_ordering.append(
                    Lower(field[1:]).desc()
                    if field.startswith('-')
                    else Lower(field).asc()
                )
            return queryset.order_by(*case_insensitive_ordering)

        return queryset
