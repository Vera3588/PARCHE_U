from django.db.models import query
from usuarios.models import Estudiante
from usuarios.models import Usuario
from usuarios.models import Gustos
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

def consultaUsuario(id):
    user = Usuario.objects.get(codigo_estudiante = id)
    info = {}
    info["codigo_estudiante"] = user.codigo_estudiante
    info["documento_identidad"] = user.documento_identidad
    info["nombre"] = user.nombre
    info["apellidos"] = user.apellidos
    info["celular"] = user.celular
    info["correo"] = user.correo
    info["carrera"] = user.carrera

    print(info)
    return info                   


def verificarGustos(criterio, tipo = 'gustos'):
    query = False
    if tipo == 'gustos':
        query = Gustos.objects.filter(codigo_estudiante_id=criterio).exists()
    return query