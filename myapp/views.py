from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Game, Post, Tournament, Profile
from .forms import PostForm, TournamentForm, ProfileSocialsForm
from django.urls import reverse

# Create your views here.

@login_required
def index(request):
    """
    Vista para la página de inicio.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        La respuesta HTTP con la plantilla 'index.html'.
    """
    return render(request, 'index.html', {   
    })

@login_required
def torneos(request):
    """
    Vista para la página de torneos.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        La respuesta HTTP con la plantilla 'torneos.html' y los torneos disponibles.
    """
    breadcrumbs = [
        {'name': 'Torneos'},
    ]
    tournaments = Tournament.objects.all()
    return render(request, 'torneos.html', {
        'breadcrumbs': breadcrumbs,
        'torneos': tournaments
    })
    
@login_required
def nuevo_torneo(request):
    """
    Vista para crear un nuevo torneo.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        La respuesta HTTP con la plantilla 'nuevo_torneo.html' y el formulario para crear un torneo.
    """
    breadcrumbs = [
        {'name': 'Torneos', 'url': reverse('torneos')},
        {'name': 'Crear Torneo'},        
    ]
    if request.method == 'POST':
        print(request.POST)
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.user = request.user
            tournament.save()
            messages.success(request, 'Torneo creado correctamente.')
            return redirect('torneos')
        else:
            messages.error(request, 'Error al crear el torneo.')
            
    form = TournamentForm()
    return render(request, 'nuevo_torneo.html', {
        'form': form,
        'breadcrumbs': breadcrumbs
    })
    
@require_POST
def inscribirse_torneo(request, id):
    """
    Vista para inscribirse a un torneo.

    Args:
        request: La solicitud HTTP recibida.
        id: El ID del torneo al que se desea inscribir.

    Returns:
        La respuesta HTTP con un mensaje de éxito o error.
    """
    tournament = Tournament.objects.get(id=id)
    if request.user in tournament.participants.all():
        messages.error(request, 'Ya estás inscrito en este torneo.')
    else:
        tournament.participants.add(request.user)
        messages.success(request, 'Te has inscrito correctamente en el torneo.')
    return redirect('torneos')


@login_required
def publicaciones(request):
    """
    Vista para la página de publicaciones.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        La respuesta HTTP con la plantilla 'publicaciones.html' y las publicaciones disponibles.
    """
    posts = Post.objects.all()
    breadcrumbs = [
        {'name': 'Publicaciones'},
    ]      
        
    return render(request, 'publicaciones.html', {
        'publicaciones': posts,
        'breadcrumbs': breadcrumbs
    })
    
@login_required
def publicar(request):
    """
    Vista para crear una nueva publicación.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        La respuesta HTTP con la plantilla 'publicar.html' y el formulario para crear una publicación.
    """
    breadcrumbs = [
        {'name': 'Publicaciones', 'url': reverse('publicaciones')},
        {'name': 'Crear Publicación'},        
    ]
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post creado correctamente.')
            return redirect('publicaciones')
        else:
            messages.error(request, 'Error al crear el post.')       
    
    form = PostForm()  
       
    return render(request, 'publicar.html', {
        'form': form,
        'breadcrumbs': breadcrumbs
    })

@login_required
def perfil(request, id):
    """
    Vista para el perfil de un usuario.

    Args:
        request: La solicitud HTTP recibida.
        id: El ID del usuario cuyo perfil se desea ver.

    Returns:
        La respuesta HTTP con la plantilla 'perfil.html' y el perfil del usuario especificado.
    """
    profile = Profile.objects.get(user_id=id)
    if request.user.id == id:
        breadcrumbs = [            
            {'name': 'Mi Perfil'},
        ]
    else:
        breadcrumbs = [
            {'name': 'Perfiles'},
            {'name': profile.user.username},
        ]
        
    return render(request, 'perfil.html', {
        'profile': profile,
        'breadcrumbs': breadcrumbs
    })

@login_required
def añadir_cuenta_social(request):
    """
    Vista para añadir una cuenta social al perfil.

    Args:
        request: La solicitud HTTP recibida.

    Returns:
        La respuesta HTTP con la plantilla 'añadir_cuenta_social.html' y el formulario para añadir una cuenta social.
    """
    breadcrumbs = [
        {'name': 'Mi Perfil', 'url': reverse('perfil', args=[request.user.id])},
        {'name': 'Añadir Cuenta Social'},        
    ]
    
    if request.method == 'POST':
        form = ProfileSocialsForm(request.POST)
        if form.is_valid():
            social = form.save(commit=False)
            social.profile = request.user.profile
            social.save()
            messages.success(request, 'Cuenta social añadida correctamente.')
            return redirect('perfil', request.user.id)
        else:
            messages.error(request, 'Error al añadir la cuenta social.')
            
    form = ProfileSocialsForm()
    return render(request, 'nueva_red_social.html', {
        'form': form,
        'breadcrumbs': breadcrumbs
    })