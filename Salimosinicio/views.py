import sqlite3

from django.shortcuts import render, render_to_response


def inicio(request):
    return render(request, "Iniciosalimos.html", {})


def formu(request):
    return render(request, 'formulario.html', {})


def llama(request):
    return render(request, "registro.html", {})


def menu(request):
    return render(request, 'main.html')


def index(request):
    return render(request, 'Eventos/Lugares/index.html')


def festiva(request):
    return render(request, 'Eventos/Festivales/Categorias.html', {})


def Lugaress(request):
    return render(request, 'Eventos/Lugares/Lugares.html', {})


def cine_list(request):
    db = sqlite3.connect(database='Salimos.db')
    cursor = db.cursor()
    cursor.execute("Select   Funcion, Fecha, Hora from Funiciones")
    Funcion = cursor.fetchall()
    db.close()
    return render_to_response('Eventos/Festivales/Categorias.html', {'Funcion': Funcion})


def Lugares_list(request):
    db = sqlite3.connect(database='Salimos.db')
    cursor = db.cursor()
    cursor.execute('Select Nombre from Lugares')
    cursor.execute('Select Ciudad from Lugares')
    Ciudad = cursor.fetchall()
    Nombre=cursor.fetchall()
    db.close()
    return render_to_response('Eventos/Lugares/Lugares.html', {'Ciudad': Ciudad}, {'Nombre': Nombre})
