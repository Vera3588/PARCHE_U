"""PARCHE_U URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name = 'inicio'),
    path('registro/', views.Registro, name ='registro'),
    path('gustos/', views.InicioApp ,name ='inicioApp'),
    path('index/', views.logout_request ,name ='cerrar_sesion'),
    path('inicio/', views.Inicio_muro, name='inicio_muro'),
    path('perfil/<int:codigo_estudiante>/', views.Perfil, name='perfil'),
    path('misGustos/', views.Gustos, name='gustos'),
    path('psicologos/', views.Psicologos, name='psicologos'),
    path('salto/', views.Salto, name='salto'),
    path('salto2/', views.Salto2, name='salto2'),
    path('editarPerfil/', views.EditarPerfil, name='editarPerfil'),
    path('editarClave/', views.EditarClave, name='editarClave'),
    path('enviar_solicitud/<int:codigo_estudiante>/', views.Enviar_solicitud, name='enviar_solicitud'),
    path('aceptar_solicitud/<int:requestID>/', views.Aceptar_solicitud, name='aceptar_solicitud'),
    
]
'''path('rechazar_solicitud/<int:requestID>/', views.Rechazar_solicitud, name='rechazar_solicitud'),'''
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)