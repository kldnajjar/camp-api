from rest_framework.routers import SimpleRouter

from camp.api import TentTypeModelViewSet, FoodModelViewSet, \
    MealTypeModelViewSet, ActivityModelViewSet, TentModelViewSet

router = SimpleRouter()
router.register("tent_types", TentTypeModelViewSet)
router.register("foods", FoodModelViewSet)
router.register("meal_types", MealTypeModelViewSet)
router.register("activities", ActivityModelViewSet)
router.register("tents", TentModelViewSet)

urlpatterns = []
urlpatterns += router.urls
