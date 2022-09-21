from django.shortcuts import render
from django.http import HttpResponse
from DataMundial.models import Registro
from DataMundial.forms import form_registros
from DataMundial.models import selecciones
from DataMundial.models import grupo

# Create your views here.

def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def inicio2(request):
    return render(request, 'inicio2.html')

########################## registro y busqueda ###############################
def registros(request):
    if request.method == "POST":
        registro= Registro(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], edad=request.POST['edad'])
        registro.save()
        return render(request, "registros.html")   
    return render(request, "registros.html")

def buscar_registro(request):
    if request.GET["email"]:
        email = request.GET["email"]
        registros = Registro.objects.filter(email__icontains = email) 
        if registros:
            return render(request, "registros.html", {"registros": registros})
        else:
            return HttpResponse("NO EXISTEN REGISTROS")
     
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
##############################################################################

def ver_selecciones(request):
    return render(request, 'selecciones.html')

def concurso(request):
    return render(request, 'concurso.html')

def pronostico(request):
    return render(request, 'pronostico.html')

def ver_argentina(request):
    Argentina = selecciones.objects.all()
    return render(request, "argentina.html",{'argentina':Argentina})