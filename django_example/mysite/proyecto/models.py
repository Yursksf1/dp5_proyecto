from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=500)
    age = models.PositiveIntegerField()

    def __str__(self):
        return "{} - {}".format(self.name, self.age)

class Game(models.Model):
    date = models.CharField(max_length=500)
    location = models.CharField(max_length=500)

    def __str__(self):
        return "{} - {}".format(self.date, self.location)