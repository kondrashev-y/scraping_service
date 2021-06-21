from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('cities', CityViewSet)
router.register('lang', LanguageViewSet)
router.register('vacancy', VacancyViewSet)
urlpatterns = router.urls
