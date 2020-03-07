from rest_framework import serializers
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


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(read_only=True)
    name = serializers.CharField(source='full_name', read_only=True)
    role = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(max_length=128, required=False)

    class Meta:
        model = User
        fields = ('id', 'name', 'first_name', 'phone_number', 'last_name',
                  'role', 'email', 'is_active')
