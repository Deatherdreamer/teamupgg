from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    """
    Representa el perfil de un usuario en la aplicación.
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)	
    country = models.CharField(max_length=100)  
    riot_puuid = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        """
        Devuelve una representación en cadena del perfil.
        """
        return self.user.first_name + ' ' + self.user.last_name
    
    def get_socials(self):
        """
        Devuelve una queryset con las redes sociales asociadas al perfil.
        """
        return ProfileSocials.objects.filter(profile=self)
    

class ProfileSocials(models.Model):
    """
    Representa las redes sociales asociadas a un perfil.
    """
    NETWORK_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('Twitch', 'Twitch'),
        ('Youtube', 'Youtube'),
        ('Discord', 'Discord'),
        ('Steam', 'Steam'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    network = models.CharField(max_length=100, choices=NETWORK_CHOICES)
    url = models.URLField()
    
    def __str__(self):
        """
        Devuelve una representación en cadena de las redes sociales asociadas al perfil.
        """
        return self.profile.user.first_name + ' ' + self.profile.user.last_name + ' | ' + self.network


class Game(models.Model):
    """
    Representa un juego en la aplicación.
    """
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """
        Devuelve una representación en cadena del juego.
        """
        return self.name
    

class Post(models.Model):
    """
    Representa una publicación en la aplicación.
    """
    title = models.CharField(max_length=100)
    message = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la publicación.
        """
        return self.title + ' | ' + str(self.user)
    

class Tournament(models.Model):
    """
    Representa un torneo en la aplicación.
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    password = models.CharField(max_length=100, blank=True, null=True)
    max_players = models.IntegerField()
    date_of_tournament = models.DateTimeField()
    participants = models.ManyToManyField(get_user_model(), related_name='participants')
    
    def signed_in_players(self):
        """
        Devuelve una queryset de todos los jugadores que se han registrado para este torneo.
        """
        return self.participants.all()
