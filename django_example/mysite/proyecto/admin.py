from django.contrib import admin
from proyecto.models import Player, Game, GamePlayer

# Register your models here.
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(GamePlayer)
