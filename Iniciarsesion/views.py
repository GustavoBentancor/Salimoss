from django.shortcuts import render


def formu(request):
    return render(request, 'formulario.html', {})