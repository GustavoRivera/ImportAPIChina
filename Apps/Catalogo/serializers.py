from rest_framework import serializers
from Apps.Catalogo.models import CatalogoModelo

class CatalogoSerialize(serializers.ModelSerializer):
    class Meta:
        model = CatalogoModelo
        fields = ['pk','codigo', 'nombre', 'detalle', 'precio','fecha','stock']