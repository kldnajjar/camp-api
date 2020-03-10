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
        for k, v in self.defaults.items():
            if k in unset_filters:
                data[k] = v
        return data
