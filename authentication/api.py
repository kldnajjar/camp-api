from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import CampTokenSerializer, UserSerializer


class CampTokenObtainPairView(TokenObtainPairView):
    serializer_class = CampTokenSerializer


class Me(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# class UsersModelViewSet(ModelViewSet):
#     permission_classes = (IsAuthenticated, DjangoModelPermissions,)
#     queryset =
