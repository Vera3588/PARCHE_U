from django.db import models

class Estudiante(models.Model):
    codigo_estudiante = models.IntegerField(primary_key=True)
    documento_identidad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
