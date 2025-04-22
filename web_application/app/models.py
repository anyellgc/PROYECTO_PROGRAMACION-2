from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
#PERFIL DE USUARIO
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jng', upload_to='users/', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Ubicación')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']
        
    def str (self):
        return self.user.username
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()
    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
    
    