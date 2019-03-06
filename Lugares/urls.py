from django.conf.urls import url
from django.contrib.sitemaps.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^Lugares$', view='Lugares', name='Lugar'),
    url(r'^listar', view='Lugares', name='Lugares'),
]
