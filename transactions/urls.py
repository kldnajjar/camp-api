from django.urls import re_path
from rest_framework.routers import SimpleRouter

from transactions.api import PaymentModelViewSet, DailyCashAPIView

router = SimpleRouter()
router.register('payments', PaymentModelViewSet)
urlpatterns = [
    re_path(r'daily/', DailyCashAPIView.as_view())
]
urlpatterns += router.urls
