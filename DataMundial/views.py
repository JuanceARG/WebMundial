from django.shortcuts import render, redirect
from django.http import HttpResponse
from DataMundial.models import Registro, Avatar, selecciones, grupo
from DataMundial.forms import form_registros, UserRegisterForm, UserEditForm, ChangePasswordForm, AvatarFormulario

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'home.html')

def inicio(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render (request, "inicio.html", {'avatar': avatar})

def inicio2(request):
    return render(request, 'inicio.html')

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
@login_required
def miSeleccion(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'miSeleccion.html', {'avatar': avatar})


def ver_grupos(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'grupos.html', {'avatar': avatar})

def ver_selecciones(request):
    equipos = grupo.objects.all()
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'selecciones.html', {'equipos': equipos, 'avatar': avatar})


@login_required
def concurso(request): 
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "concurso.html", {'avatar': avatar})
@login_required
def pronostico(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'pronostico.html', {'avatar': avatar})

###################Muestra la seleccion elegida en template selecciones###############
@login_required
def detalle_seleccion(request, seleccion_seleccion):
    verSeleccion = selecciones.objects.filter(seleccion = seleccion_seleccion)
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render (request, "seleccionElegida.html", {'seleccion':verSeleccion, 'avatar': avatar} )

###########login, regsitro users y modificacion users##################

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username = user, password = pwd)
            if user is not None:
                login(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render (request, "inicio.html", {'avatar': avatar})
            else:
                return render (request, "login.html", {'form': form})
        else:
            return render (request, "login.html", {'form': form})
    form = AuthenticationForm()
    return render(request, "login.html", {'form': form})



def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data("username")
            form.save()
            return redirect("/DataMundial/login/")
        else:
            return render(request, "registro.html", {'form':form})
    form = UserRegisterForm()
    return render(request, "registro.html", {'form':form})

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render (request, "inicio.html", {'avatar': avatar})
        else:
            return render (request, "editarPerfil.html", {'form':form})
    else:
        form = UserEditForm(initial = {'username': usuario.username, 'email': usuario.email})
    return render (request, 'editarPerfil.html', {'form':form, 'usuario': usuario})


@login_required
def changePass(request):
    usuario = request.user
    if request.method == "POST":  
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render (request, "inicio.html", {'avatar': avatar})
    else:        
        form = ChangePasswordForm(user = request.user)
    return render(request, "changepass.html", {'form': form, 'usuario': usuario})

########## funcion avatar#############
@login_required
def AgregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None            
            return render (request, "inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render (request, "AgregarAvatar.html", {'form': form})