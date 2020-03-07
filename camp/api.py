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


class FoodModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = FoodSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Food.objects.all()


class MealTypeModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = MealTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = MealType.objects.all()


class ActivityModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Activity.objects.all()


class TentModelViewSet(ArchivableMixin, ModelViewSet):
    serializer_class = TentSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Tent.objects.all()

# TODO
# 4. Filtering for all APIs.
# 8. Daily Cash
