# cursos/admin.py
from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista
    list_display = ('nombre', 'categoria', 'duracion_horas', 'precio', 'activo', 'fecha_creacion')
    
    # Ordenar por fecha de creación de más antiguo a más reciente
    ordering = ('fecha_creacion',)
    
    # Barra de búsqueda (busca en nombre y categoría)
    search_fields = ('nombre', 'categoria')
    
    # Filtros laterales (filtra por activo y categoría)
    list_filter = ('activo', 'categoria', 'fecha_creacion')
    
    # Campos que se muestran y etiquetas en el formulario de registro/edición
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'categoria', 'duracion_horas', 'precio', 'activo')
        }),
        ('Imágenes y fechas', {
            'fields': ('imagen', 'fecha_creacion'),
            'description': 'Campos automáticos y de imagen'
        }),
    )
    
    readonly_fields = ('fecha_creacion',)  # Campo automático, solo lectura

