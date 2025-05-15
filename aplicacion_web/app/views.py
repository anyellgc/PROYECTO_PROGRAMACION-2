# File: aplicacion_web/app/views.py
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import FormularioUsuario
from django.contrib.auth import authenticate, login
# Create your views here.
from .models import Curso, Tarea, Proyecto
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Evento 
from django.http import Http404
from .models import Recurso
from .forms import recursoForm
from .models import Calificacion, Estudiante
from .forms import CalificacionForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden



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
    
    curso=Curso.objects.create(codigo=codigo, nombre=nombre, cupos=cupos)
    messages.success(request, "Curso registrado exitosamente")
    return redirect('/')

def edicionCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request, 'app/edicionCurso.html', {'curso': curso})

def cambiarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']	
    cupos=request.POST['numCupos']
    
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

def calendario_view(request):
    return render(request, 'app/calendario.html')

def eventos_json(request):
    eventos = Evento.objects.all()
    data = []
    for evento in eventos:
        data.append({
            'title': evento.titulo,
            'start': evento.inicio.isoformat(),
            'end': evento.fin.isoformat(),
            'color': evento.color,
        })
    return JsonResponse(data, safe=False)

def eliminar_calificacion(request, calificacion_id):
    if request.method == 'POST':
        calificacion = Calificacion.objects.get(id=calificacion_id)
        calificacion.delete()
        return redirect('ver_calificaciones') 

    return HttpResponseForbidden("Método no permitido.")


@login_required
def ver_calificaciones(request):
    estudiante = Estudiante.objects.get(user=request.user)  
    calificaciones = Calificacion.objects.filter(estudiante=estudiante)  
    return render(request, 'app/ver_calificaciones.html', {
        'calificaciones': calificaciones
    })
    
@login_required
def registrar_calificacion(request):
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(user=request.user)  
        curso_codigo = request.POST.get('curso')  
        nota = request.POST.get('nota')
        observaciones = request.POST.get('observaciones')

        
        curso = Curso.objects.get(codigo=curso_codigo)  

        
        calificacion, created = Calificacion.objects.update_or_create(
            estudiante=estudiante, curso=curso,
            defaults={'nota': nota, 'observaciones': observaciones}
        )

        if created:
            messages.success(request, 'Calificación registrada exitosamente.')
        else:
            messages.success(request, 'Calificación actualizada exitosamente.')

        return redirect('ver_calificaciones')

    else:
        cursos = Curso.objects.all()  
        return render(request, 'app/registrar_calificacion.html', {'cursos': cursos})

       

@login_required
def ver_asignaciones(request):
    cursos = Curso.objects.all()
    tareas = Tarea.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, 'app/asignacion.html', {
        'cursos': cursos,
        'tareas': tareas,
        'proyectos': proyectos,
    })

@csrf_exempt
def guardar_asignacion(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            tipo = data.get("tipo")
            titulo = data.get("titulo")
            descripcion = data.get("descripcion")
            fecha_entrega = data.get("fecha_entrega")
            curso_codigo = data.get("curso")

            curso = Curso.objects.get(codigo=curso_codigo)

            if tipo == "tarea":
                Tarea.objects.create(
                    titulo=titulo,
                    descripcion=descripcion,
                    fecha_entrega=fecha_entrega,
                    curso=curso
                )
            elif tipo == "proyecto":
                Proyecto.objects.create(
                    nombre=titulo,
                    descripcion=descripcion,
                    fecha_entrega=fecha_entrega,
                    curso=curso
                )
            else:
                return JsonResponse({"success": False, "message": "Tipo no válido"})

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"success": False, "message": "Método no permitido"})

@csrf_exempt
def guardar_entrega(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "message": "Método no permitido"})

@csrf_exempt
def eliminar_asignacion(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            asignacion_id = data.get("id")
            tipo = data.get("tipo")

            if tipo == "tarea":
                tarea = Tarea.objects.get(id=asignacion_id)
                tarea.delete()
            elif tipo == "proyecto":
                proyecto = Proyecto.objects.get(id=asignacion_id)
                proyecto.delete()
            else:
                return JsonResponse({"success": False, "message": "Tipo no válido"})

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"success": False, "message": "Método no permitido"})


    
def recurso(request):
    if request.method == 'POST':
        form = recursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recurso')  
    else:
        form = recursoForm()

    recursos = Recurso.objects.all()

    return render(request, 'app/recurso.html', {
        'form': form,
        'recursos': recursos,
    })

def eliminar_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)
    recurso.delete()
    return redirect('recursos')


def estadisticas(request):
    return render(request, 'app/estadisticas.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '').lower()

        if 'hola' in user_message:
            response = '¡Hola! ¿Cómo puedo ayudarte con tus tareas?'
        elif 'tarea' in user_message:
            response = 'Puedes ver tus tareas en la sección "Mis tareas".'
        elif 'gracias' in user_message:
            response = '¡De nada! Para eso estoy.'
        elif 'cómo estás' in user_message or 'como estas' in user_message:
            response = 'Estoy muy bien, ¿y tú?'
        elif 'adiós' in user_message or 'chao' in user_message:
            response = '¡Hasta luego! :)'
        else:
            response = 'No entendí eso. Intenta otra vez.'

        return JsonResponse({'response': response})

    
    return render(request, 'app/chat.html')
   
   