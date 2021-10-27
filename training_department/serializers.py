from .models import *
from rest_framework import serializers


class CabinetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cabinet
        fields = ['name', 'number', 'fk_territory', ]


class TerritorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Territory
        fields = ['name', 'address', ]
