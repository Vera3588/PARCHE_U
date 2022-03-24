import usuarios.autenticacion as user
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from usuarios import models
import sqlite3
from PIL import Image

login_check = False
def Inicio(request):
    global login_check
    if login_check:
        return render(request, 'inicio.html')

    if request.method == 'POST':
        try:
            detalleUsuario = models.Usuario.objects.get(correo = request.POST['correo'], password = request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['correo'] = detalleUsuario.correo
            request.session['nombre'] = detalleUsuario.nombre
            request.session['codigo_estudiante'] = detalleUsuario.codigo_estudiante
            login_check = True
            return render(request, 'inicio.html')
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

        print(codigo_estudiante, documento_identidad, nombre, apellidos, celular, carrera, correo, password, password_repeat)
        if password != password_repeat:
            messages.info(request, 'Las contraseñas no coinciden')
        
        elif len(password) <= 7:
            messages.info(request, 'La contraseña debe contener por lo menos 8 caracteres')

        elif not (user.verificarCarrera(carrera) or user.verificarCodigoEstudiante(codigo_estudiante) or user.verificarCorreo(correo) or user.verificarDocumento(documento_identidad)):
            messages.info(request, 'No perteneces a la Universidad o revisa la informacion nuevamente')

        elif user.verificarPrevioRegistro(codigo_estudiante):
            messages.info(request,'Usuario ya registrado, por favor inicia sesión')

        
        elif user.verificarCarrera(carrera) and user.verificarCodigoEstudiante(codigo_estudiante) and user.verificarCorreo(correo) and user.verificarDocumento(documento_identidad):
            agregar = models.Usuario(codigo_estudiante = codigo_estudiante, documento_identidad = documento_identidad,
            nombre = nombre, apellidos = apellidos, celular = celular, carrera = carrera, correo = correo,
            password = password, password_repeat = password_repeat)
            agregar.save()
            return render(request, 'inicio.html')

    return render(request, 'registro.html')

def InicioApp(request):
    codigo = request.session['codigo_estudiante']

    if user.verificarGustos(codigo):
        return render(request, 'inicio.html')
    else:
        if request.method =='POST':   
            musica = request.POST['musica']
            deportes = request.POST['deportes']
            series = request.POST['series']
            videojuegos = request.POST['videojuegos']
            literatura = request.POST['literatura']

            agregar = models.Gustos(musica = musica, deportes = deportes, series=series,videojuegos=videojuegos,
            literatura = literatura,codigo_estudiante_id = codigo)
            agregar.save()
            return Inicio_muro(request)
        return render(request, 'inicioapp.html')

def Inicio_muro(request):
    return render(request, 'inicio.html')

def Perfil(request):
    codigo = request.session['codigo_estudiante']
    info_usuario = user.consultaUsuario(codigo)
    return render(request, "perfil.html", {"info_usuario": info_usuario})