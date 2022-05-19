from django.db.models import query

from usuarios.models import Estudiante
from usuarios.models import Usuario
from usuarios.models import Gustos, Psicologo, Publicaciones
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
    es_usuario = Usuario.objects.filter(codigo_estudiante = id).exists()
    es_psicologo = Psicologo.objects.filter(cedula = id).exists()
    if es_usuario:
        user = Usuario.objects.get(codigo_estudiante = id)
        info = {}
        info["codigo_estudiante"] = user.codigo_estudiante
        info["documento_identidad"] = user.documento_identidad
        info["nombre"] = user.nombre
        info["apellidos"] = user.apellidos
        info["celular"] = user.celular
        info["correo"] = user.correo
        info["carrera"] = user.carrera
    elif es_psicologo:
        user = Psicologo.objects.get(cedula=id)
        info = {}
        info["codigo_estudiante"] = user.cedula
        info["nombre"] = user.nombre
        info["apellidos"] = user.apellidos
        info["correo"] = user.correo
    print(info)
    return info   

def consultaGusto(id):
    user = Gustos.objects.get(codigo_estudiante = id)
    info = {}
    info["musica"] = user.musica
    info["deportes"] = user.deportes
    info["series"] = user.series
    info["videojuegos"] = user.videojuegos
    info["literatura"] = user.literatura

    print(info)
    return info                   


def verificarGustos(criterio, tipo = 'gustos'):
    query = False
    if tipo == 'gustos':
        query = Gustos.objects.filter(codigo_estudiante_id=criterio).exists()
    return query

def verificarPsicologo(criterio, tipo = 'psicologo'):
    query = False
    if tipo == 'psicologo':
        query = Psicologo.objects.filter(correo=criterio).exists()
    return query

def actualizarUsuario(id, nombre, apellidos, celular):
    target = Usuario.objects.get(codigo_estudiante = id)
    target.nombre = nombre
    target.apellidos = apellidos
    target.celular = celular
    target.save(update_fields=['nombre', 'apellidos', 'celular'])

def verificarClave(id, password, tipo = 'usuario'):
    query = False
    # mirar posibilidad de consulta sql SELECT * FROM usuario_usuarios WHERE codigo_estudiante = 'id' AND password = 'password';
    if tipo == 'usuario':
        query = Usuario.objects.filter(password=password, codigo_estudiante = id).exists()
    return query

def actualizarClave(id,password_new):
    target = Usuario.objects.get(codigo_estudiante = id)
    target.password = password_new
    target.save(update_fields=['password'])

def consultaPublicacion():
    publicacion = Publicaciones.objects.all()

    #print(info)
    #return info   