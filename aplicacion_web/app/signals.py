from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save  

from .models import Perfil, Estudiante

from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save  
from .models import Perfil, Estudiante

@receiver(post_save, sender=Perfil)
def crear_modelo_por_grupo(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        try:
            estudiante_group = Group.objects.get(name='estudiante')
        except Group.DoesNotExist:
            estudiante_group = Group.objects.create(name='estudiante')
            Group.objects.create(name='docentes')
            Group.objects.create(name='administrativo')
        
        user.groups.add(estudiante_group)
        user.save()

        # Crear modelo Estudiante si el usuario está en el grupo 'estudiante'
        if user.groups.filter(name='estudiante').exists():
            Estudiante.objects.create(user=user)
        
