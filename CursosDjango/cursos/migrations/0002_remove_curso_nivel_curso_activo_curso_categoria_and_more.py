# Generated by Django 5.0.6 on 2025-06-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='nivel',
        ),
        migrations.AddField(
            model_name='curso',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Curso activo'),
        ),
        migrations.AddField(
            model_name='curso',
            name='categoria',
            field=models.CharField(default='General', max_length=50, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='duracion_horas',
            field=models.PositiveIntegerField(verbose_name='Duración (horas)'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cursos/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre del Curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Precio'),
        ),
    ]
