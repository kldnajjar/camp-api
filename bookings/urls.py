from rest_framework.routers import SimpleRouter

from bookings.api import FoodReservationModelViewSet, \
    StayReservationModelViewSet, ReservorModelViewSet, StayTypeModelViewSet, \
    ReservationTypeModelViewSet

router = SimpleRouter()

router.register("reservation_types", ReservationTypeModelViewSet)
router.register("stay_types", StayTypeModelViewSet)
router.register("reservors", ReservorModelViewSet)
router.register("stay_reservations", StayReservationModelViewSet)
router.register("food_reservations", FoodReservationModelViewSet)
urlpatterns = []
urlpatterns += router.urls
