from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.api import CampTokenObtainPairView, Me

urlpatterns = [
    path('', CampTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', Me.as_view(), name='my_info'),
]
