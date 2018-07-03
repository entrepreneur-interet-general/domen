from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

from .models import Location
from .search_index import LocationIndex


class LocationSerializer(HaystackSerializer):

    class Meta:
        index_classes = [LocationIndex]
        fields = [
            "text", "address", "city", "zip_code", "autocomplete"
        ]


class LocationSearchView(HaystackViewSet):

    index_models = [Location]
    serializer_class = LocationSerializer
