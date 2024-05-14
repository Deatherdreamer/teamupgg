from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('torneos/', torneos, name='torneos'),
    path('torneos/<int:id>/inscribirse/', inscribirse_torneo, name='inscribirse_torneo'),
    path('torneos/nuevo-torneo/', nuevo_torneo, name='nuevo_torneo'),
    path('publicaciones/', publicaciones , name='publicaciones'),
    path('publicaciones/nueva-publicacion/', publicar , name='publicar'),
    
    path('perfil/<int:id>/', perfil , name='perfil'),
    path('perfil/nuevo-social/', añadir_cuenta_social , name='añadir_cuenta_social'),
]
    
    