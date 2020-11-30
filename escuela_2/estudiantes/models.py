from django.db import models
from clases.models import Clase

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    estatus = models.CharField(max_length=200)
    carrera = models.CharField(max_length=200)
    creditos = models.CharField(max_length=200) 
    clases = models.ManyToManyField(Clase, through=u'ListaClases', related_name='clase')
    
    def __str__(self):
        return self.nombre

class ListaClases(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)