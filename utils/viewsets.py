from rest_framework.mixins import DestroyModelMixin


class ArchivableMixin(DestroyModelMixin):
    def perform_destroy(self, instance):
        instance.archived = True
        instance.save()
