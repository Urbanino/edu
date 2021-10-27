from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EquipmentSerializer
from .models import Equipment


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows equipment to be viewed or edited
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]
