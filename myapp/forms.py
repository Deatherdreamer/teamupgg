from django import forms
import django.contrib
from .models import Post, Game, Profile, Tournament
from allauth.account.forms import SignupForm
from django.contrib import messages
import datetime

class MyCustomSignupForm(SignupForm):
    email = forms.EmailField(
        max_length=254,
        label='Correo',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}),
        help_text='Ingrese su correo'
    )
    first_name = forms.CharField(
        max_length=30,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
        help_text='Ingrese su nombre'
    )
    last_name = forms.CharField(
        max_length=30,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
        help_text='Ingrese su apellido'
    )
    nickname = forms.CharField(
        max_length=100,
        label='Apodo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apodo'}),
        help_text='Ingrese su apodo'
    )
    date_of_birth = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su fecha de nacimiento', 'type': 'date'}),
        help_text='Ingrese su fecha de nacimiento'
    )
    country = forms.CharField(
        max_length=100,
        label='Pais',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su país'}),
        help_text='Ingrese su país'
    )
    gender = forms.ChoiceField(
        label='Genero',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        help_text='Seleccione su genero',
    )
    

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        
        #dont save if user under 18
        if self.cleaned_data['date_of_birth'] > datetime.date.today() - datetime.timedelta(days=365.25*18):
            messages.error(request, "You must be over 18 to register")
            raise forms.ValidationError("You must be over 18 to register")
        
        
        user = super(MyCustomSignupForm, self).save(request)
        user.username = self.cleaned_data['nickname']
        user.save()
        
        # Add your own processing here.
        
        
        
        profile = Profile.objects.create(
            user=user,
            date_of_birth=self.cleaned_data['date_of_birth'],
            country=self.cleaned_data['country'],
            gender=self.cleaned_data['gender'],
            nickname=self.cleaned_data['nickname']
        )
        
        profile.save()
        
              

        # You must return the original result.
        return user

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