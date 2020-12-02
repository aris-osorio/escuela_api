from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from profesores.models import Profesor
from profesores.serializers import ProfesorSerializer

class Profesores(APIView):
    def get(self, request, format=None):
        profesores = Profesor.objects.all()
        serializer = ProfesorSerializer(profesores, many=True)
        return Response(status = status.HTTP_200_OK, data = serializer.data)

    def post(self, request, format=None):
        serializer = ProfesorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleProfesor(APIView):
    def get_object(self, id):
        try:
            return Profesor.objects.get(id = id)
        except Profesor.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        profesor = self.get_object(id)
        serializer = ProfesorSerializer(profesor)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        Profesor = self.get_object(id)
        serializer = ProfesorSerializer(Profesor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        profesor = self.get_object(id)
        profesor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)