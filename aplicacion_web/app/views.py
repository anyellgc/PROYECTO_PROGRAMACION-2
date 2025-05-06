# File: aplicacion_web/app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import FormularioUsuario
from django.contrib.auth import authenticate, login
# Create your views here.
from .models import Curso
from django.contrib import messages


def registro(request):
    return render(request, 'app/registro.html')

@login_required
def inicio(request):
    cursosListados = Curso.objects.all()
    messages.success(request, "Bienvenido a la plataforma de cursos")
    return render(request, 'app/inicio.html', {"cursos": cursosListados})

def exit(request):
    logout(request)
    return redirect('registro')

def registrer(request):
    data = {
        'form': FormularioUsuario()
    }

    if request.method == 'POST':
        user_creation_form = FormularioUsuario(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password2'])
            login(request, user)

            return redirect('registro')

    return render(request, 'app/registrer.html', data)
# Create your views here.
def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']	
    cupos=request.POST['numCupos']
    
    curso=Curso.objects.create(
        codigo=codigo, nombre=nombre, cupos=cupos)
    messages.success(request, "Curso registrado exitosamente")
    return redirect('/')

def edicionCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request, 'app/edicionCurso.html', {'curso': curso})

def editarCurso(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']	
    cupos=request.POST['numCreditos']
    
    curso=Curso.objects.get(codigo=codigo)
    curso.nombre=nombre
    curso.cupos=cupos
    curso.save()
    
    messages.success(request, "Curso actualizado exitosamente")
    
    return redirect('/')
    
def eliminarCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    
    messages.success(request, "Curso eliminado exitosamente")
    
    return redirect('/')

