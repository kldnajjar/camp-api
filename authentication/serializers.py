from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentication.models import User


class CampTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['phone_number'] = user.phone_number
        try:
            token['roles'] = list(user.groups.values_list('name', flat=True))[0]
        except IndexError as _error:
            pass
        return token


class MeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    role = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(max_length=128, required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'phone_number', 'last_name',
                  'role', 'email', 'is_active')


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[
        UniqueValidator(User.objects.all(), _("User already registered."))
    ])
    role = serializers.CharField()
    phone_number = serializers.CharField(max_length=128, required=False)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        role = validated_data.pop('role', 'employee')
        password = validated_data.pop('password', None)
        if not password:
            raise ValidationError({
                'password': _("This is a required field.")
            })
        user = super().create(validated_data)
        user.role = role
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        role = validated_data.pop('role', 'employee')
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        if role:
            user.role = role
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'phone_number', 'last_name',
                  'role', 'email', 'is_active', 'password')
