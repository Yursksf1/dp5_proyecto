from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Player


def index(request):
    personas = Player.objects.all()

    # ejemplo con string:
    messaje = "Lista de jugadores"
    for persona in personas:
        messaje = messaje + "<br> {}".format(persona.name)

    contexto = {
        "nombre": "Yurley",
        "nombres": ["yurley",  "camilo", "garcia"]
    }

    return render(request, 'index.html', contexto)