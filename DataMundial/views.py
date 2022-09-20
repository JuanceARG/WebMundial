from django.shortcuts import render
from django.http import HttpResponse
from DataMundial.models import Registro
from DataMundial.forms import form_registro
from DataMundial.models import selecciones
from DataMundial.models import grupo

# Create your views here.

def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def inicio2(request):
    return render(request, 'inicio2.html')

def registro(request):
    if request.method == "POST":
        registrar = Registro(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], edad=request.POST['edad'])
        registrar.save()
        return render(request, "registro.html")   
    return render(request, "registro.html")

def ver_selecciones(request):
    return render(request, 'selecciones.html')

def concurso(request):
    return render(request, 'concurso.html')

def pronostico(request):
    return render(request, 'pronostico.html')

def ver_argentina(request):
    Argentina = selecciones.objects.all()
    return render(request, "argentina.html",{'argentina':Argentina})