from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre