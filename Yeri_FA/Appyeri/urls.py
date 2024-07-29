from django.urls import path
from Appyeri import views

urlpatterns = [ 
    path('', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name='Profesores'),
    path('alumnos/', views.alumnos, name='Alumnos'),
    path('practicas/', views.practicas, name='Practicas'),
    path('sugerencias/', views.sugerencias, name='Sugerencias'),
]
