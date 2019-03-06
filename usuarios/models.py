from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200)

    def _unicode_(self):
        return self.nombre
