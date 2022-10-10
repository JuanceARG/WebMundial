from turtle import home
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from DataMundial.views import *

urlpatterns = [
    path('', inicio),
    path('DataMundial/', inicio),
    path('inicio/', inicio),
    path('inicio2/', inicio2),
    path('registros/', registros),
    path('selecciones/', ver_selecciones),
    path('grupos/', ver_grupos),
    path('login/', login_request),
    path('registro/', registro),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/changepass/', changePass),
    path('logout/', LogoutView.as_view(template_name='inicio.html')),
    path('concurso/', concurso),
    path('miseleccion/', miSeleccion),
    path('perfil/changeAvatar', AgregarAvatar),
    path('pronostico/', pronostico),    
    path('seleccionElegida/<seleccion_seleccion>', detalle_seleccion),
    path('buscar_registro/', buscar_registro),
]