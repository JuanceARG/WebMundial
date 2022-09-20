from socket import fromshare
from django import forms

class form_registro(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()