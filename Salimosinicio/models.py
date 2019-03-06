from django.views import View
from django.db import models
from django.forms import ModelForm


class TopicView(View):
    template_name = "Iniciosalimos.html"


class Categorias(models.Model):
    Categorias = models.CharField(max_length=500)

    def __unicode__(self):
        return self.Categorias


