from distutils.command.upload import upload
from django.db import models

class Estudiante(models.Model):
    codigo_estudiante = models.IntegerField(primary_key=True)
    documento_identidad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

class Usuario(models.Model):
    codigo_estudiante = models.IntegerField(primary_key=True)
    documento_identidad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    celular = models.IntegerField()
    carrera = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    password_repeat = models.CharField(max_length=20)
    #foto_perfil = models.ImageField(upload_to='usuarios/images/foto_perfil/',null=True)
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

class Gustos(models.Model):
    musica = models.CharField(max_length=500, null=True)
    deportes = models.CharField(max_length=500, null=True)
    series = models.CharField(max_length=500, null=True)
    videojuegos = models.CharField(max_length=500, null=True)
    literatura = models.CharField(max_length=500, null=True)
    codigo_estudiante = models.ForeignKey(Usuario,on_delete = models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = "gusto"
        verbose_name_plural = "gustos"

'''
class Publicaciones(models.Model):
    id_publicacion = models.IntegerField(primary_key=True)
    mensaje = models.CharField(max_length=1000, null=False)
    imagen = models.ImageField(upload_to='usuarios/images/publicaciones/', null=True)
    codigo_estudiante = models.ForeignKey(Usuario,on_delete = models.CASCADE, null=True, blank=True)

class Comentarios

'''