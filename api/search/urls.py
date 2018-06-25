from django.conf.urls import url, include
from rest_framework import routers

from .views import LocationSearchView

router = routers.DefaultRouter()
router.register("search", LocationSearchView, base_name="search")


urlpatterns = [
    url(r"", include(router.urls)),
]
