from django.db import models


class Character(models.Model):
    class Status(models.TextChoices):
        ALIVE = 'A', 'Alive'
        DEAD = 'D', 'Dead'
        UNKNOWN = 'U', 'Unknown'

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        GENDERLESS = 'G', 'Genderless'
        UNKNOWN = 'U', 'Unknown'

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=Status.choices)
    species = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=Gender.choices)
    image = models.URLField(max_length=500, unique=True)

    def __str__(self):
        return self.name



