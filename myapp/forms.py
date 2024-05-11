from django import forms
from .models import Post

#Crear un formularios
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'message', 'game']
        labels = {
            'title': 'Titulo',
            'message': 'Mensaje',
            'game': 'Juego'
        }
        help_texts = {
            'title': 'El titulo del post',
            'message': 'El mensaje del post',
            'game': 'El juego al que pertenece el post'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'game': forms.Select(attrs={'class': 'form-control'})
        }