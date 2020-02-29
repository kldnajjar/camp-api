from rest_framework import serializers

from camp.models import Activity, TentType, Food, MealType, Tent


class TentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TentType
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class MealTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealType
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class TentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tent
        fields = '__all__'
