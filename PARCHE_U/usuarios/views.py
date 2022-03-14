from django.shortcuts import render
from django.http import HttpResponse

def Inicio(request):
    return render(request, 'index.html')

def Registro(request):
    return render(request, 'registro.html')