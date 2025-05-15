"""
URL configuration for aplicacion_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
"""
URL configuration for web_application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path
from . views import estadisticas,registro, inicio, exit, registrer , chatbot_response, eventos_json, calendario_view, ver_asignaciones, ver_calificaciones
from . import views 
from django.contrib.auth.decorators import login_required
from . views import recurso
from django.conf import settings

urlpatterns = [
   path('', registro, name='registro'),
   path('inicio', inicio, name='inicio'),
   path('exit/', exit, name='exit'),
   path('registrer/', registrer, name='registrer'),
   #-----------------------------------------------------------
   #parte de nuevo curso donde se empieza a modificar el codigo
   path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
   path('edicionCurso/<codigo>', views.edicionCurso, name='edicionCurso'),
   path('cambiarCurso/', views.cambiarCurso, name='cambiarCurso'),  
   path('eliminarCurso/<codigo>', views.eliminarCurso, name='eliminarCurso'),
   path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
   path('eventos/', views.eventos_json, name='eventos_json'),
   path('inicio/calendario.html/', calendario_view, name='calendario'),
   path('inicio/ver_calificaciones/',ver_calificaciones, name='ver_calificaciones'), 
   path('inicio/asignacion.html/', ver_asignaciones, name='ver_asignaciones'), 
   path('inicio/estadisticas.html/', estadisticas, name='estadisticas'),
   path('inicio/recurso.html/',recurso, name='recurso'),
   path('asignaciones/', views.ver_asignaciones, name='asignaciones'),
   path('ver_calificaciones/', views.ver_calificaciones, name='ver_calificaciones'),
   path('inicio/registrar_calificacion.html/', views.registrar_calificacion, name='registrar_calificacion'),
   path('guardar_asignacion/', views.guardar_asignacion, name='guardar_asignacion'),
   path('guardar-entrega/', views.guardar_entrega, name='guardar_entrega'),
   path('eliminar-asignacion/', views.eliminar_asignacion, name='eliminar_asignacion'),
   path('eliminar-recurso/<int:recurso_id>/', views.eliminar_recurso, name='eliminar_recurso'),
   path('eliminar_calificacion/<int:calificacion_id>/', views.eliminar_calificacion, name='eliminar_calificacion'),
]

