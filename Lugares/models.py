from django.db import models


class Lugar(models.Model):
    nombre = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=10)
    Direccion = models.CharField(max_length=150)
    Fecha = models.CharField(max_length=150)
    Telefono = models.CharField(max_length=150)
    Pagina = models.CharField(max_length=150)


class Cines (models.Model):
    nombre = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=10)
    Direccion = models.CharField(max_length=150)
    Fecha = models.CharField(max_length=150)
    Telefono = models.CharField(max_length=150)
    Pagina = models.CharField(max_length=150)


