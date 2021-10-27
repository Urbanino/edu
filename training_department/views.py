from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CabinetSerializer, TerritorySerializer
from .models import *


class CabinetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cabinet to be viewed or edited
    """
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    permission_classes = [permissions.IsAuthenticated]


class TerritoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cabinet to be viewed or edited
    """
    queryset = Territory.objects.all()
    serializer_class = TerritorySerializer
    permission_classes = [permissions.IsAuthenticated]
