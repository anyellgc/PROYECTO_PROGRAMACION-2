from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioUsuario(UserCreationForm):
	

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]
  

from .models import Recurso

class recursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nombre', 'archivo', 'descripcion']
        
        
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['curso', 'nota', 'observaciones']