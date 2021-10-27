from .models import *
from rest_framework import serializers


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name', 'model', 'code', 'fk_cabinet']

