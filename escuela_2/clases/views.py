from clases.models import Clase
from clases.serializers import ClaseSerializer
from rest_framework import generics


class Clases(generics.ListCreateAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer


class DetalleClase(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer