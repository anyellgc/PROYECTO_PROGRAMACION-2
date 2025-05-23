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
from . views import registro, inicio, exit, registrer
from . import views 

urlpatterns = [
   path('', registro, name='registro'),  # URL for the registro view
   path('inicio/', inicio, name='inicio'),
   path('exit/', exit, name='exit'),  # URL for the exit view
   path('registrer/', registrer, name='registrer'),
   #-----------------------------------------------------------
   #parte de nuevo curso donde se empieza a modificar el codigo
   path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
   path('edicionCurso/<codigo>', views.editarCurso, name='editarCurso'),
   path('editarCurso/', views.editarCurso, name='editarCurso'),  
   path('eliminarCurso/<codigo>', views.eliminarCurso, name='eliminarCurso'),
   
]   