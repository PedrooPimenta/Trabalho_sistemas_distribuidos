from api.serializers import MonografiaSerializer
from django.shortcuts import render
from rest_framework import viewsets, permissions
from monografias.models import Monografia
# Create your views here.


class MonografiaViewSet(viewsets.ModelViewSet):
    queryset = Monografia.objects.all()
    serializer_class = MonografiaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
