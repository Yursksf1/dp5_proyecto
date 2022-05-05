class People:
    """
    this class persona
    """

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    @staticmethod
    def get_user_by_id(id, list_player):
        person = None

        for player in list_player:
            if id == player.id:
                person = player

        return person

class Game:
    """
    this class about games
    """

    def __init__(self, id, date, location):
        self.id = id
        self.date = date
        self.location = location

    @staticmethod
    def get_game_by_id(id, list_game):
        game = None

        for juego in list_game:
            if id == juego.id:
                game = juego

        return game

class GamePlayer:
    """
    this class about point in a specific game and specific person
    """

    def __init__(self, person, game, point, fail):
        self.game = game
        self.person = person
        self.point = point
        self.fail = fail

    def anotacion(self, new_point):
        self.point = self.point + new_point

    def fall(self, new_fail):
        self.fail = self.fail + new_fail

    @staticmethod
    def get_point_by_game(points):
        puntos_por_partidos = {}
        for point in points:
            if point.game.date not in puntos_por_partidos:
                puntos_por_partidos[point.game.date] = 0
            puntos_por_partidos[point.game.date] = puntos_por_partidos[point.game.date] + point.point

        return puntos_por_partidos

people_1 = People(id="J1", name="Yurley", age=13)
people_2 = People(id="J2", name="Maria", age=18)
people_3 = People(id="J3", name="Jose", age=15)
people_4 = People(id="J4", name="Diego", age=16)
people_5 = People(id="J5", name="Daniel", age=16)
people_6 = People(id="J6", name="Marcos", age=19)
people_7 = People(id="J7", name="Isabella", age=12)
people_8 = People(id="J8", name="Cristian", age=17)
people_9 = People(id="J9", name="Gustavo", age=16)
people_10 = People(id="J10", name="Luisa", age=18)

list_player = [
    people_1,
    people_2,
    people_3,
    people_4,
    people_5,
    people_6,
    people_7,
    people_8,
    people_9,
    people_10
    ]

game_1 = Game(id="G1", date="10/01/22", location="Cancha 1")
game_2 = Game(id="G2", date="15/01/22", location="Cancha 2")
game_3 = Game(id="G3", date="20/01/22", location="Cancha 1")
game_4 = Game(id="G4", date="25/01/22", location="Cancha 2")
game_5 = Game(id="G5", date="30/01/22", location="Cancha 2")
game_6 = Game(id="G6", date="5/02/22", location="Cancha 2")
game_7 = Game(id="G7", date="10/02/22", location="Cancha 3")
game_8 = Game(id="G8", date="15/02/22", location="Cancha 1")

list_games = [
    game_1,
    game_2,
    game_3,
    game_4,
    game_5,
    game_6,
    game_7,
    game_8,
    ]

lista_game_players = []
lista_game_players.append(GamePlayer(people_1, game_1, 0, 2))
lista_game_players.append(GamePlayer(people_2, game_1, 10, 0))
lista_game_players.append(GamePlayer(people_3, game_1, 2, 0))
lista_game_players.append(GamePlayer(people_4, game_1, 0, 1))
lista_game_players.append(GamePlayer(people_5, game_1, 3, 0))
lista_game_players.append(GamePlayer(people_1, game_2, 2, 0))
lista_game_players.append(GamePlayer(people_3, game_2, 20, 3))
lista_game_players.append(GamePlayer(people_5, game_2, 2, 0))
lista_game_players.append(GamePlayer(people_7, game_2, 3, 0))
lista_game_players.append(GamePlayer(people_9, game_2, 0, 0))
lista_game_players.append(GamePlayer(people_2, game_3, 0, 0))
lista_game_players.append(GamePlayer(people_4, game_3, 3, 0))
lista_game_players.append(GamePlayer(people_6, game_3, 2, 2))
lista_game_players.append(GamePlayer(people_8, game_3, 11, 0))
lista_game_players.append(GamePlayer(people_10, game_3, 2, 0))
lista_game_players.append(GamePlayer(people_3, game_4, 3, 1))
lista_game_players.append(GamePlayer(people_4, game_4, 0, 0))
lista_game_players.append(GamePlayer(people_5, game_4, 0, 0))
lista_game_players.append(GamePlayer(people_9, game_4, 12, 3))
lista_game_players.append(GamePlayer(people_10, game_4, 2, 0))
lista_game_players.append(GamePlayer(people_3, game_5, 3, 0))
lista_game_players.append(GamePlayer(people_4, game_5, 2, 0))
lista_game_players.append(GamePlayer(people_5, game_5, 3, 0))
lista_game_players.append(GamePlayer(people_6, game_5, 0, 0))
lista_game_players.append(GamePlayer(people_7, game_5, 0, 2))
lista_game_players.append(GamePlayer(people_1, game_6, 3, 0))
lista_game_players.append(GamePlayer(people_2, game_6, 2, 0))
lista_game_players.append(GamePlayer(people_5, game_6, 3, 1))
lista_game_players.append(GamePlayer(people_8, game_6, 2, 0))
lista_game_players.append(GamePlayer(people_10, game_6, 10, 0))
lista_game_players.append(GamePlayer(people_3, game_7, 0, 3))
lista_game_players.append(GamePlayer(people_5, game_7, 0, 0))
lista_game_players.append(GamePlayer(people_6, game_7, 3, 0))
lista_game_players.append(GamePlayer(people_7, game_7, 2, 0))
lista_game_players.append(GamePlayer(people_10, game_7, 3, 0))
lista_game_players.append(GamePlayer(people_1, game_8, 2, 0))
lista_game_players.append(GamePlayer(people_5, game_8, 3, 1))
lista_game_players.append(GamePlayer(people_6, game_8, 0, 2))
lista_game_players.append(GamePlayer(people_9, game_8, 2, 3))
lista_game_players.append(GamePlayer(people_10, game_8, 6, 4))


jugadores = {
}


# Here is my menu
menu = """
    Selecciona la opcion que desea realizar  
    1. Desea ingresar un nuevo jugador.
    2. Desea ingresar los datos de un nuevo juego.
    3. Desea ingresar los datos de un jugador en un juego.
    4. Imprimir resultados.
    5. Imprimir todos los jugadores.
    6. Imprimir todos los juegos.
    0. SALIR.
"""

bandera = True
while bandera:
    respuesta = input(menu)
    if respuesta == '0':
        bandera = False

    elif respuesta == '1':
        print("=== ingresando nuevo jugador === ")
        nombre = input("Ingresa el nombre del nuevo jugador: ")
        age = input("Ingresa la eded de {}: ".format(nombre))
        id = "J{}".format(len(list_player)+1)
        list_player.append(People(id=id, name=nombre, age=age))

    elif respuesta == '2':
        print("=== ingresando nuevo juego === ")
        date = input("Ingresa la fecha del juego: ")
        location = input("Ingresa la ubicacion donde se juego: ")
        id = "G{}".format(len(list_games)+1)
        list_games.append(Game(id=id, date=date, location=location))


    elif respuesta == '3':
        print("=== ingresando nuevos datos de jugador en juego === ")
        jugador_id = input("Ingresa el id del jugador: ")
        people = People.get_user_by_id(jugador_id, list_player)
        if people:
            print(people.name, people.age)

        game_id = input("Ingresa el id del juego: ")
        game = Game.get_game_by_id(game_id, list_games)
        if game:
            print(game.location, game.date)

        puntos = int(input("Ingresa los puntos que anoto "))
        faltas = int(input("Ingresa las faltas que cometio "))
        lista_game_players.append(GamePlayer(people, game, puntos, faltas))

    elif respuesta == '4':
        print("=== Resultados === ")

        for lista_game_player in lista_game_players:
            name = lista_game_player.person.name
            if name not in jugadores:
                jugadores[name] = {
                    "id": lista_game_player.person.id,
                    'person': lista_game_player.person,
                    "partidos_jugados": 0,
                    "faltas_totales": 0,
                    "puntos_totales": 0,
                    "promedio": 0,
                }
            jugadores[name]["partidos_jugados"] = jugadores[name]["partidos_jugados"] + 1
            jugadores[name]["faltas_totales"] = jugadores[name]["faltas_totales"] + lista_game_player.fail
            jugadores[name]["puntos_totales"] = jugadores[name]["puntos_totales"] + lista_game_player.point
            jugadores[name]["promedio"] = jugadores[name]["puntos_totales"] / jugadores[name]["partidos_jugados"]

        lista_clasificacion = []


        for jugador, data in jugadores.items():
            if data["partidos_jugados"] >= 3 and data["faltas_totales"] < 10 and data["person"].age >= 15:
                lista_clasificacion.append({"jugador": jugador, "promedio": data["promedio"]})


        lista_clasificacion = sorted(lista_clasificacion, key=lambda d: -d['promedio'])

        for jugador in lista_clasificacion[:5]:
            print(jugador)

    elif respuesta == '5':
        print("=== imprimiendo todos los jugadores === ")
        for jugador in list_player:
            print(jugador.id, jugador.name, jugador.age)

    elif respuesta == '6':
        print("=== imprimiendo todos los juegos === ")
        for juego in list_games:
            print(juego.id, juego.location, juego.date)