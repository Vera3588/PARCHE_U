from dataclasses import fields
from django import forms
from usuarios.models import Usuario

class ActualizarImagenForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['foto_perfil']

