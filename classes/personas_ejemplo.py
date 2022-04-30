class People:
    """
    this class persona
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update_information(self, *arg, **kw):
        if "name" in kw:
            self.name = kw.get("name")

        if "age" in kw:
            self.age = kw.get("age")


class Game:
    """
    this class about games
    """

    def __init__(self, date, location):
        self.date = date
        self.location = location


class Points:
    """
    this class about point in a specific game and specific person
    """

    def __init__(self, game, person):
        self.game = game
        self.person = person
        self.point = 0

    def anotacion(self, new_point):
        self.point = self.point + new_point

people_1 = People(name="Yurley", age=15)
people_2 = People(name="Diego", age=17)
people_3 = People(name="Yeimi", age=16)
people_4 = People(name="Vale", age=16)
people_5 = People(name="Jose", age=14)

game = Game(date="el 1 de abril del 2022", location="cancha numero 1")

point_d = Points(game=game, person=people_2)
point_d.anotacion(new_point=3)
point_d.anotacion(new_point=2)
point_d.anotacion(new_point=2)

point_y = Points(game=game, person=people_3)
point_y.anotacion(new_point=2)
point_y.anotacion(new_point=3)
point_y.anotacion(new_point=3)


game_2 = Game(date="el 4 de abril del 2022", location="cancha numero 3")
point_y_1 = Points(game=game_2, person=people_1)
point_y_1.anotacion(new_point=2)
point_y_1.anotacion(new_point=2)

point_j = Points(game=game_2, person=people_5)
point_j.anotacion(new_point=3)
point_j.anotacion(new_point=3)

points = [point_d, point_y, point_y_1, point_j]

for point in points:
    # print("INFORMACION DE DIEGO")
    print("la persona: {},  anoto {} puntos en el partido que se llevo acabo el dia {}, en la cancha {}".format(
        point.person.name, point.point, point.game.date, point.game.location,
    ))


"""
Ejercicio 2: 
Agregar un nuevo partido de baloncesto. 
agregar un nuevo integrante del  equipo.
agregar minimo 4 anotacion por cada persona. 

"""