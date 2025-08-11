from django.db import models
from ckeditor.fields import RichTextField

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

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]

    def __str__(self):
        return self.coment
