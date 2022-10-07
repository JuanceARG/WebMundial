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
    path('grupos/', ver_grupos),
    path('concurso/', concurso),
    path('pronostico/', pronostico),    
    path('seleccionElegida/<seleccion_seleccion>', detalle_seleccion),
    path('buscar_registro/', buscar_registro),
]