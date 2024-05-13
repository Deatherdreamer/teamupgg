from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)	
    country = models.CharField(max_length=100)  
    riot_puuid = models.CharField(max_length=100, blank=True, null=True)
    
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
class ProfileSocials(models.Model):
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
        return self.profile.user.first_name + ' ' + self.profile.user.last_name + ' | ' + self.network

class Game(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + str(self.user)
    
class Tournament(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    password = models.CharField(max_length=100, blank=True, null=True)
    max_players = models.IntegerField()
    date_of_tournament = models.DateTimeField()
    participants = models.ManyToManyField(get_user_model(), related_name='participants')
    
    
    
    

    
    
