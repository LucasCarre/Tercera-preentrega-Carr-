from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'appyeri/inicio.html')

def cursos(request):
    return render(request, 'appyeri/cursos.html')

def profesores(request):
    return render(request, 'appyeri/profesores.html')

def alumnos(request):
    return render(request, 'appyeri/alumnos.html')

def practicas(request):
    return render(request, 'appyeri/practicas.html')

def sugerencias(request):
    return render(request, 'appyeri/sugerencias.html')