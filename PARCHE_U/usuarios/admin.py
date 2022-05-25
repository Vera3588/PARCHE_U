from django.contrib import admin
from .models import Publicaciones, Usuario, Psicologo

#admin.site.register(Estudiante)
admin.site.register(Usuario)
admin.site.register(Publicaciones)
admin.site.register(Psicologo)

