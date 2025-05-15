from django.db import models
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

#parte de nuevo curso donde se empieza a modificar el codigo   
class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, verbose_name='Código de categoría')
    nombre = models.CharField(max_length=50)
    cupos =models.PositiveSmallIntegerField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.cupos)
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
#calendario
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    color = models.CharField(max_length=7, default='#3788d8')  # color del evento

    def __str__(self):
        return self.titulo
    
class Recurso(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='recursos/')
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante} - {self.curso.nombre}: {self.nota}"
    

