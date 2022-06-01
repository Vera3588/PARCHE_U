from distutils.command.upload import upload
from django.db import models


'''class Estudiante(models.Model):
    codigo_estudiante = models.IntegerField(primary_key=True)
    documento_identidad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"'''

class Usuario(models.Model):
    codigo_estudiante = models.IntegerField(primary_key=True)
    documento_identidad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    celular = models.IntegerField()
    carrera = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    amigos = models.ManyToManyField("Usuario", blank = True, related_name = "lista_amigos")
    foto_perfil = models.ImageField(upload_to='foto_perfil/', default='foto_perfil/nullprofile.jpg')
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


class Publicaciones(models.Model):
    id_publicacion = models.IntegerField(primary_key=True)
    mensaje = models.CharField(max_length=1000, null=False)
    imagen = models.FileField(upload_to='publicaciones/', null=True)
    fecha_publicacion = models.CharField(max_length=10,null=False)
    hora_publicacion = models.CharField(max_length=10,null=False)
    codigo_estudiante = models.ForeignKey(Usuario,on_delete = models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = "publicacion"
        verbose_name_plural = "publicaciones"

class Psicologo(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    class Meta:
        verbose_name = "psicologo"
        verbose_name_plural = "psicologos"

class Solicitud_Amistad(models.Model):
    usuario_envia = models.ForeignKey(Usuario, related_name='usuario_envia', on_delete=models.CASCADE, related_query_name="enviador")
    usuario_recibe = models.ForeignKey(Usuario, related_name='usuario_recibe', on_delete=models.CASCADE, related_query_name="recibidor")
    class Meta:
        verbose_name = "solicitud"
        verbose_name_plural = "solicituds"

class Mensaje(models.Model):
    id_mensaje = models.IntegerField(primary_key=True)
    mensaje = models.CharField(max_length=1000, null=False)
    fecha_publicacion = models.CharField(max_length=10,null=False)
    hora_publicacion = models.CharField(max_length=10,null=False)
    usuario_envia = models.ForeignKey(Usuario, related_name='usuario_enviador', on_delete=models.CASCADE)
    usuario_recibe = models.ForeignKey(Usuario, related_name='usuario_recibidor', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "mensaje"
        verbose_name_plural = "mensajes"