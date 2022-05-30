from wsgiref.util import request_uri
from usuarios.models import Solicitud_Amistad
from usuarios.models import Publicaciones, Usuario
from .forms import ActualizarImagenForm
from matplotlib.ft2font import HORIZONTAL
import usuarios.autenticacion as user
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib import messages
from usuarios import models
import sqlite3
from PIL import Image
import cv2
from datetime import datetime


login_check = False
def Inicio(request):
    global login_check
    if login_check:
        return render(request, 'inicio.html')
    if request.method == 'POST':
        if request.POST['correo'] == "crear@psicologo.com" and request.POST['password'] == "1234" :
            login_check = False
            return render(request, 'salto.html')
        else:
            try:
                detalleUsuario = models.Usuario.objects.get(correo = request.POST['correo'], password = request.POST['password'])
                print("Usuario=", detalleUsuario)
                request.session['correo'] = detalleUsuario.correo
                request.session['nombre'] = detalleUsuario.nombre
                request.session['codigo_estudiante'] = detalleUsuario.codigo_estudiante
                login_check = True
                return render(request, 'salto2.html')
            except models.Usuario.DoesNotExist as e:
                messages.info(request, "Correo y/o contraseña no son correctos")
    return render(request, 'index.html')

def logout_request(request):
    global login_check
    login_check = False
    return Inicio(request)

def Registro(request):
    if request.method =='POST':
        codigo_estudiante = request.POST['codigo_estudiante']
        documento_identidad = request.POST['documento_identidad']
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        celular = request.POST['celular']
        carrera = request.POST['carrera']
        correo = request.POST['correo']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        print(codigo_estudiante, documento_identidad, nombre, apellidos, celular, carrera, correo, password)
        if password != password_repeat:
            messages.info(request, 'Las contraseñas no coinciden')
        
        elif len(password) <= 7:
            messages.info(request, 'La contraseña debe contener por lo menos 8 caracteres')
        
            '''elif not (user.verificarCarrera(carrera) or user.verificarCodigoEstudiante(codigo_estudiante) or user.verificarCorreo(correo) or user.verificarDocumento(documento_identidad)):
                messages.info(request, 'No perteneces a la Universidad o revisa la informacion nuevamente')'''
        
        elif user.verificarPrevioRegistro(codigo_estudiante):
            messages.info(request,'Usuario ya registrado, por favor inicia sesión')

        
        else: #if user.verificarCarrera(carrera) and user.verificarCodigoEstudiante(codigo_estudiante) and user.verificarCorreo(correo) and user.verificarDocumento(documento_identidad):
            agregar = models.Usuario(codigo_estudiante = codigo_estudiante, documento_identidad = documento_identidad,
            nombre = nombre, apellidos = apellidos, celular = celular, carrera = carrera, correo = correo,
            password = password)
            agregar.save()
            return Inicio(request)

    return render(request, 'registro.html')

def InicioApp(request):
    codigo = request.session['codigo_estudiante']

    if user.verificarGustos(codigo):
        info_usuario = user.consultaUsuario(codigo)
        return Gustos(request)
    else:
        if request.method =='POST':   
            musica = request.POST['musica']== 'actualizar'
            deportes = request.POST['deportes']
            series = request.POST['series']
            videojuegos = request.POST['videojuegos']
            literatura = request.POST['literatura']

            agregar = models.Gustos(musica = musica, deportes = deportes, series=series,videojuegos=videojuegos,
            literatura = literatura,codigo_estudiante_id = codigo)
            agregar.save()
            info_usuario = user.consultaUsuario(codigo)
            return Inicio_muro(request,{'info_usuario':info_usuario})
        info_usuario = user.consultaUsuario(codigo)
        return render(request, 'inicioapp.html',{'info_usuario':info_usuario})

def Inicio_muro(request):
    codigo = request.session['codigo_estudiante']

    if request.method =='POST':
        now = datetime.now()
        mensaje = request.POST['mensaje']
        dia = now.day
        mes = now.month
        año = now.year

        fecha= f'{año}-{mes}-{dia}'
        
        hora = now.hour
        minutos = now.minute
        segundos = now.second

        tiempo = f'{hora}:{minutos}:{segundos}'

        if not request.POST['imagen'] == None:
            imagen = request.POST['imagen']
        agregar = models.Publicaciones(mensaje = mensaje, imagen = imagen, fecha_publicacion = fecha, hora_publicacion = tiempo, codigo_estudiante_id = codigo)
        agregar.save()
        return Salto2(request)
    publicaciones =reversed(Publicaciones.objects.filter(codigo_estudiante_id = codigo))
    publicaciones1 = Usuario.objects.filter(codigo_estudiante = codigo)
    solicitudes = Solicitud_Amistad.objects.filter(usuario_recibe_id = codigo)
    info_usuario = user.consultaUsuario(codigo)
    return render(request, 'inicio.html',{"publicaciones": publicaciones, "info_usuario":info_usuario, "solicitudes":solicitudes,"publicaciones1": publicaciones1,})

def Perfil(request, codigo_estudiante):
        es_estudiante = models.Usuario.objects.filter(codigo_estudiante=codigo_estudiante).exists()
        es_psicologo = models.Psicologo.objects.filter(cedula=codigo_estudiante).exists()
        if es_psicologo == True:
            codigo_actual = request.session['codigo_estudiante']
            info_usuario = user.consultaUsuario(codigo_estudiante)
            usuario_actual = user.consultaUsuario(codigo_actual)
            return render(request, "perfilpsicologo.html", {"info_usuario":info_usuario, "usuario_actual":usuario_actual})
        elif es_estudiante == True:
            info_usuario = user.consultaUsuario(codigo_estudiante)
            info_usuario1 = models.Usuario.objects.get(codigo_estudiante = codigo_estudiante)
            codigo_actual = request.session['codigo_estudiante']
            usuario_actual = user.consultaUsuario(codigo_actual)
            usuario_actual_1 = models.Usuario.objects.get(codigo_estudiante = codigo_actual)
            hay_amistad = user.hayAmistad(codigo_estudiante, codigo_actual)
            hay_solicitud = models.Solicitud_Amistad.objects.filter(usuario_envia_id = codigo_actual, usuario_recibe_id = codigo_estudiante).exists()
            solicitudesRecibe = models.Solicitud_Amistad.objects.filter(usuario_recibe_id = codigo_actual)
            return render(request, "perfil.html", {"info_usuario":info_usuario, "usuario_actual":usuario_actual, "hay_solicitud":hay_solicitud, "hay_amistad":hay_amistad, "solicitudesRecibe":solicitudesRecibe, "amigos":hay_amistad})
        else:
            html = "<html><body>El usuario no existe</body></html>"
            return HttpResponse(html)

def Gustos(request):
    codigo = request.session['codigo_estudiante']
    info_gustos = user.consultaGusto(codigo)
    info_usuario = user.consultaUsuario(codigo)
    return render(request, 'gustos.html', {"info_gustos":info_gustos, "info_usuario":info_usuario})

def Psicologos(request):
    if request.method =='POST':
        cedula = request.POST['cedula']
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        password = request.POST['password']
        if not user.verificarPsicologo(correo):
            agregar = models.Psicologo(cedula = cedula, nombre = nombre, apellidos = apellidos,correo = correo, password = password)
            agregar.save()
            return render(request, 'inicioPsicologo.html', {"cedula":cedula})
    return render(request, 'registroPsicologos.html')


def Salto(request):
    return render(request, 'salto.html')

def Salto2(request):
    return render(request, 'salto2.html')

def SaltoEditar(request, codigo):
    return render(request, 'saltoeditarperfil.html', {"codigo":codigo})
def SaltoInicioPsicologos(request):
    return render(request, 'saltoInicioPsicologos.html')

def EditarClave(request):
    codigo = request.session['codigo_estudiante']
    if request.method == 'POST':
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        password_new = request.POST['password_new']

        if password_new != password_repeat:
            messages.info(request, 'Las nuevas contraseñas no coinciden')
        elif password == password_new:
            messages.info(request,'La contraseña nueva no puede ser igual a la actual') 
        elif len(password_new) <= 7:
            messages.info(request, 'La contraseña debe contener por lo menos 8 caracteres')
        elif not user.verificarClave(codigo, password):
            messages.info(request,'Contraseña actual incorrecta')
        else:
            user.actualizarClave(codigo, password_new)
            return SaltoEditar(request,codigo)
    info_usuario = user.consultaUsuario(codigo)
    return render(request,'editarClave.html', {"info_usuario":info_usuario})

def EditarPerfil(request):
    codigo = request.session['codigo_estudiante']
    info_usuario = user.consultaUsuario(codigo)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        celular = request.POST['celular']
        user.actualizarUsuario(codigo,nombre,apellidos,celular)
        return SaltoEditar(request,codigo)
    return render(request, 'editarPerfil.html',{"info_usuario": info_usuario})
import os
def EditarImagen(request):
    codigo = request.session['codigo_estudiante']
    info_usuario = user.consultaUsuario(codigo)
    usuario = models.Usuario.objects.get(codigo_estudiante=codigo)
    if request.method == 'POST':
        foto_form = ActualizarImagenForm(request.POST, request.FILES, instance=usuario)
        if foto_form.is_valid():
            foto_form.save()
            messages.success(request, f'Se ha actualizado tu foto')
            return SaltoEditar(request,codigo)
    else:
        foto_form=ActualizarImagenForm(request.POST, request.FILES, instance=usuario)
    return render(request, 'editarImagen.html',{"info_usuario": info_usuario, 'foto_form':foto_form})

def Enviar_solicitud(request, codigo_estudiante):
        codigo_actual = request.session['codigo_estudiante']
        usuario_envia = models.Usuario.objects.get(codigo_estudiante=codigo_actual)
        usuario_recibe = models.Usuario.objects.get(codigo_estudiante = codigo_estudiante)
        solicitud_amistad, created = models.Solicitud_Amistad.objects.get_or_create(usuario_envia=usuario_envia, usuario_recibe=usuario_recibe)
        if created:
            messages.success(request, 'solicitud de amistad enviada')
            return Perfil(request, codigo_estudiante=codigo_estudiante)
        else:
            messages.success(request, 'solicitud de amistad enviada anteriormente')
            return Perfil(request, codigo_estudiante=codigo_estudiante)

def Aceptar_solicitud(request, requestID):
    solicitud_amistad = models.Solicitud_Amistad.objects.get(id=requestID)
    if not solicitud_amistad.usuario_recibe == request.user:
        solicitud_amistad.usuario_recibe.amigos.add(solicitud_amistad.usuario_envia)
        solicitud_amistad.usuario_envia.amigos.add(solicitud_amistad.usuario_recibe)
        solicitud_amistad.delete()
        return Perfil(request, solicitud_amistad.usuario_recibe.codigo_estudiante)
    else:
        return Perfil(request, solicitud_amistad.usuario_recibe.codigo_estudiante)

def Rechazar_Solicitud(request, requestID):
    solicitud_amistad = models.Solicitud_Amistad.objects.get(id=requestID)
    if not solicitud_amistad.usuario_recibe == request.user:
        solicitud_amistad.delete()
        return Perfil(request, solicitud_amistad.usuario_recibe.codigo_estudiante)
    else:
        return Perfil(request, solicitud_amistad.usuario_recibe.codigo_estudiante)

def InicioPsicologos(request):
    return render(request, 'inicioPsicologo.html')

def Amigos(request):
    codigo = request.session['codigo_estudiante']
    info_usuario = user.consultaUsuario(codigo)
    amigos = Usuario.objects.filter(lista_amigos__in = [codigo])
    solicitudesRecibe = models.Solicitud_Amistad.objects.filter(usuario_recibe_id = codigo)
    return render(request, 'amigos.html', {'amigos':amigos, 'info_usuario':info_usuario, 'solicitudes':solicitudesRecibe})