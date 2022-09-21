from turtle import home
from django.contrib import admin
from django.urls import path,include
from DataMundial.views import *

urlpatterns = [
    path('', inicio),
    path('DataMundial/', inicio),
    path('inicio/', inicio),
    path('registros/', registros),
    path('selecciones/', ver_selecciones),
    path('concurso/', concurso),
    path('pronostico/', pronostico),
    path('argentina/', ver_argentina),
    path('buscar_registro/', buscar_registro),
]