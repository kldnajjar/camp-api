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
