from rest_framework.viewsets import ModelViewSet

from camp.models import TentType, Food, MealType, Activity, Tent
from camp.serializers import TentSerializer, TentTypeSerializer, FoodSerializer, \
    MealTypeSerializer, ActivitySerializer


class TentTypeModelViewSet(ModelViewSet):
    serializer_class = TentTypeSerializer
    queryset = TentType.objects.all()
    pagination_class = None


class FoodModelViewSet(ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class MealTypeModelViewSet(ModelViewSet):
    serializer_class = MealTypeSerializer
    queryset = MealType.objects.all()
    pagination_class = None


class ActivityModelViewSet(ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    pagination_class = None


class TentModelViewSet(ModelViewSet):
    serializer_class = TentSerializer
    queryset = Tent.objects.all()
