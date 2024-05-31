from api.serializers import MonografiaSerializer, PesquisadorSerializer
from django.shortcuts import render
from rest_framework import viewsets, permissions
from equipe.models import Pesquisador
from monografias.models import Monografia
# Create your views here.


class MonografiaViewSet(viewsets.ModelViewSet):
    queryset = Monografia.objects.all()
    serializer_class = MonografiaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PesquisadorViewSet(viewsets.ModelViewSet):
    queryset = Pesquisador.objects.all()
    serializer_class = PesquisadorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]