from django.db.models import query
from usuarios.models import Estudiante
from usuarios.models import Usuario
import sqlite3

def verificarPrevioRegistro(criterio, tipo = 'usuario'):
    query = False
    if tipo == 'usuario':
        query = Usuario.objects.filter(codigo_estudiante=criterio).exists()
    return query

def verificarCodigoEstudiante(criterio, tipo = 'estudiante'):
    query = False
    if tipo == 'estudiante':
        query = Estudiante.objects.filter(codigo_estudiante=criterio).exists()
    return query

def verificarCorreo(criterio, tipo = 'estudiante'):
    query = False
    if tipo == 'estudiante':
        query = Estudiante.objects.filter(correo=criterio).exists()
    return query

def verificarDocumento(criterio, tipo = 'estudiante'):
    query = False
    if tipo == 'estudiante':
        query = Estudiante.objects.filter(documento_identidad=criterio).exists()
    return query

def verificarCarrera(criterio, tipo = 'estudiante'):
    query = False
    if tipo == 'estudiante':
        query = Estudiante.objects.filter(carrera=criterio).exists()
    return query