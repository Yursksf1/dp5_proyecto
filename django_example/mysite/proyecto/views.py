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



def hola_mundo_123(request):
    print("estoy llamado a la ruta 123")
    return render(request, 'index.html', {})


def players(request):
    personas = Player.objects.all()

    # here is the magic
    context = {
        "personas": [{'name': p.name, "age": p.age} for p in personas]
    }

    if request.method == 'POST':
        data = request.POST
        player_age = data.get('player_age')
        player_name = data.get('player_name')

        # TODO: create a record in model
        print("Voy a agregar un registro al modelo player con estos atributos: ")
        print("player_age:", player_age)
        print("player_name:", player_name)


    return render(request, "players.html", context)