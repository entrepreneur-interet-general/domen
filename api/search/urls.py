from django.conf.urls import url, include
from rest_framework import routers

from .views import ColonneViewset

router = routers.DefaultRouter()
router.register("search/colonnes", ColonneViewset, base_name="colonnes")

urlpatterns = [
    url(r"", include(router.urls)),
]
