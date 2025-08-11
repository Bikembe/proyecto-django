from django.contrib import admin
from .models import Curso
from .models import Comentario

admin.site.site_header = "Panel de Administración"
admin.site.site_title = "Cursos | Admin"
admin.site.index_title = "Bienvenido al panel de gestión"


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'duracion_horas', 'precio', 'activo', 'fecha_creacion')
    ordering = ('fecha_creacion',)
    search_fields = ('nombre', 'categoria')
    list_filter = ('activo', 'categoria', 'fecha_creacion')
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'categoria', 'duracion_horas', 'precio', 'activo')
        }),
        ('Imágenes y fechas', {
            'fields': ('imagen', 'fecha_creacion'),
            'description': 'Campos automáticos y de imagen'
        }),
    )
    
    readonly_fields = ('fecha_creacion',)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields = ('id','created')
    date_hierarchy = ('created')
    readonly_fields = ('created','id')

admin.site.register(Comentario,AdministrarComentarios)

