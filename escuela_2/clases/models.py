from django.db import models
from profesores.models import Profesor

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=200)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    dia = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)
    creditos = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre