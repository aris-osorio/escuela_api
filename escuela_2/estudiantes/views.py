from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from estudiantes.models import Estudiante
from estudiantes.models import ListaClases
from estudiantes.serializers import EstudianteSerializer
from estudiantes.serializers import ListaClaseSerializer


@api_view(['GET', 'POST'])
def Estudiantes(request):
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EstudianteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def DetalleEstudiante(request, id):
    try:
        estudiante = Estudiante.objects.get(id = id)
    except estudiante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EstudianteSerializer(estudiante, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        estudiante.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

