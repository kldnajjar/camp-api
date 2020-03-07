from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from camp.models import Food, MealType, Activity, Tent, TentType
from camp.serializers import TentSerializer, FoodSerializer, \
    MealTypeSerializer, ActivitySerializer, TentTypeSerializer
from utils.viewsets import ArchivableMixin


class TentTypeModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = TentTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = TentType.objects.all()
    pagination_class = None


class FoodModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = FoodSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Food.objects.all()


class MealTypeModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = MealTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = MealType.objects.all()
    pagination_class = None


class ActivityModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Activity.objects.all()
    pagination_class = None


class TentModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = TentSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Tent.objects.all()

# TODO
# 2. Make Validation Error with a single format.
# 3. Make Pagination single format.
# 8. Daily Cash
