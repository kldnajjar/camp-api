from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from camp.models import TentType, Food, MealType, Activity, Tent
from camp.serializers import TentSerializer, TentTypeSerializer, FoodSerializer, \
    MealTypeSerializer, ActivitySerializer


class TentTypeModelViewSet(ModelViewSet):
    serializer_class = TentTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = TentType.objects.all()
    pagination_class = None


class FoodModelViewSet(ModelViewSet):
    serializer_class = FoodSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Food.objects.all()


class MealTypeModelViewSet(ModelViewSet):
    serializer_class = MealTypeSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = MealType.objects.all()
    pagination_class = None


class ActivityModelViewSet(ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Activity.objects.all()
    pagination_class = None


class TentModelViewSet(ModelViewSet):
    serializer_class = TentSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = Tent.objects.all()
