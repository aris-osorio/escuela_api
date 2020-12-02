from django.urls import path
from profesores import views

urlpatterns = [
    path('' , views.Profesores.as_view()),
    path('<int:id>/' , views.DetalleProfesor.as_view())
]

