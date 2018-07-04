from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Colonne


class ColonneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colonne
        fields = '__all__'


class ColonneViewset(viewsets.ModelViewSet):

    serializer_class = ColonneSerializer
    queryset = Colonne.objects.all()
    pagination_class = PageNumberPagination
