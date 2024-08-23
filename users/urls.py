from django.urls import path
from .views import listarPersonas, crearPersonas

urlpatterns = [
    path('', listarPersonas, name='listarPersonas'),
    path('crear/', crearPersonas, name='crearPersonas'),
]