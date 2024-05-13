from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Game, Post, Tournament, Profile
from .forms import PostForm

# Create your views here.

@login_required
def index(request):

    return render(request, 'index.html', {   
    })

@login_required
def torneos(request):
    return render(request, 'torneos.html')

@login_required
def publicaciones(request):
    posts = Post.objects.all()
    
    return render(request, 'publicaciones.html', {
        'publicaciones': posts
    })
    
@login_required
def publicar(request):
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
        'form': form
    })

@login_required
def perfil(request, id):
    profile = Profile.objects.get(user_id=id)
    return render(request, 'perfil.html', {
        'profile': profile
    })
