from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def alumnos(request):
    return HttpResponse("Vista estudiantes")

def practicas(request):
    return HttpResponse("Vista practicas")

def sugerencias(request):
    return HttpResponse("Vista sugerencias")