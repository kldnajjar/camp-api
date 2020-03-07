from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from authentication.models import User
from authentication.serializers import UserSerializer
from utils.viewsets import ModifiedQuerysetMixin, ExcludeHttpMethodsMixin


class UserModelViewSet(ExcludeHttpMethodsMixin('PUT'),
                       ModifiedQuerysetMixin,
                       ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (DjangoModelPermissions,)

    def get_modified_queryset(self, queryset):
        return queryset.exclude(id=self.request.user.id)
