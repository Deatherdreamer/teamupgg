from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser




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
    
    
    
    

    
    
