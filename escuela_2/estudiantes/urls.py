from django.urls import path
from estudiantes import views

urlpatterns = [
    path('' , views.Estudiantes),
    path('<int:id>/' , views.DetalleEstudiante)
]

