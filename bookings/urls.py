from rest_framework.routers import SimpleRouter

from bookings.api import FoodReservationModelViewSet, StayReservationModelViewSet, \
    CompanyModelViewSet, StayTypeModelViewSet

router = SimpleRouter()

router.register("stay_types", StayTypeModelViewSet)
router.register("companies", CompanyModelViewSet)
router.register("stay_reservations", StayReservationModelViewSet)
router.register("food_reservations", FoodReservationModelViewSet)
urlpatterns = []
urlpatterns += router.urls
