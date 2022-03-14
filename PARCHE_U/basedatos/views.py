from django.shortcuts import render
from django.http import HttpResponse

def Inicio(request):
    return render(request, 'inicio.html',{'name':'Cristian d'})
