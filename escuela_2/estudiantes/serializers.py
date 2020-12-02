from rest_framework import serializers
from estudiantes.models import Estudiante
from estudiantes.models import ListaClases

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class ListaClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaClases
        fields = '__all__'