from turtle import home
from django.contrib import admin
from django.urls import path,include
from DataMundial.views import *

urlpatterns = [
    path('', home),
    path('DataMundial/', home)
]