from django.contrib import admin
from .models import Perfil
#----------------------------------------------------------
from .models import Curso
from .models import Estudiante, Calificacion, Curso, Tarea, Proyecto


# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'location', 'telephone', 'user_group')
    search_fields = ('user__username', 'address', 'user__groups__name')
    list_filter = ('user__groups', 'location')
    
    def user_group(self, obj):
        return "- ".join([group.name for group in obj.user.groups.all().order_by('name')])
    
    user_group.short_description = 'Grupo de usuario'
    
    
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Calificacion)
admin.site.register(Tarea)
admin.site.register(Proyecto)



