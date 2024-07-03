from django.db import models

from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=200)
    año = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.marca.nombre} - {self.año})"
