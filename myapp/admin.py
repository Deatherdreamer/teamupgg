from django.contrib import admin
from .models import Game, Post, Tournament

# Register your models here.
admin.site.register(Game)
admin.site.register(Post)
admin.site.register(Tournament)

