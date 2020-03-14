from rest_framework.routers import SimpleRouter

from transactions.api import PaymentModelViewSet

router = SimpleRouter()
router.register('payments', PaymentModelViewSet)
urlpatterns = []
urlpatterns += router.urls
