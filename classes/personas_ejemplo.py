class People:
    """
    this class persona
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.num_juegos = 0

    def update_information(self, *arg, **kw):
        if "name" in kw:
            self.name = kw.get("name")

        if "age" in kw:
            self.age = kw.get("age")

    def get_number_character_of_name(self):
        return len(self.name)

    def jugo(self):
        print("agregamos un juego mas")
        self.num_juegos = self.num_juegos + 1


persona_1 = People(name="Yurley", age=30)
print(persona_1.name, persona_1.get_number_character_of_name())
persona_1.jugo()
persona_1.jugo()
persona_1.jugo()

persona_2 = People(name="Diego", age=25)
print(persona_2.name, persona_2.get_number_character_of_name())
persona_2.jugo()
persona_2.jugo()

persona_3 = People(name="Yerly", age=15)
print(persona_3.name, persona_3.get_number_character_of_name())
persona_3.jugo()
persona_3.jugo()
persona_3.jugo()
persona_3.jugo()
persona_3.jugo()






print(persona_1.name, persona_1.num_juegos)
print(persona_2.name, persona_2.num_juegos)
print(persona_3.name, persona_3.num_juegos)


"""
Ejercicio:
en base a este objeto persona -- (jugador)
agregar un atributo de numero de anotaciones
y agregar una funcion para sacar el promedio de anotacion por partido.

"""