from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField("Nombre del Curso", max_length=100)
    descripcion = models.TextField("Descripción", blank=True, null=True)
    duracion_horas = models.PositiveIntegerField("Duración (horas)")
    precio = models.DecimalField("Precio", max_digits=8, decimal_places=2)
    activo = models.BooleanField("Curso activo", default=True)
    categoria = models.CharField("Categoría", max_length=50, default="General")
    imagen = models.ImageField("Imagen", upload_to="cursos/", blank=True, null=True)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.nombre