from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('torneos/', torneos, name='torneos'),
    path('publicaciones/', publicaciones , name='publicaciones'),
    path('publicaciones/nueva-publicacion/', publicar , name='publicar'),
    
    path('perfil/<int:id>/', perfil , name='perfil'),
]
    
    