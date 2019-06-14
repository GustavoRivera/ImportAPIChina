from django.db import models

# Create your models here.

class CatalogoModelo(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre