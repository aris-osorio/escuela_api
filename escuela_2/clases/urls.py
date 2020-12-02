from django.urls import path
from clases import views

urlpatterns = [
    path('' , views.Clases.as_view()),
    path('<int:pk>/' , views.DetalleClase.as_view())
]

