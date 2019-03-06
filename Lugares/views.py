from django.shortcuts import render
from Lugares.models import Lugar, Cines
from Lugares.models import Lugar


def lugares_list(request):
    Lugar.objects.all().order_by('id')
    contexto = {'Lugares': Lugar}
    return render(request, 'Eventos/Lugares/list_lugares.html', contexto)


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    nombre = nombre.objects.all().count()
    telefono = telefono.objects.all().count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )
