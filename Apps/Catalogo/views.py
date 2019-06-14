from django.shortcuts import render

from rest_framework import viewsets

from Apps.Catalogo.models import CatalogoModelo
from Apps.Catalogo.serializers import CatalogoSerialize

class CatalogoView(viewsets.ModelViewSet):
    queryset = CatalogoModelo.objects.all()
    serializer_class = CatalogoSerialize
