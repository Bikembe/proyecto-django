from django.shortcuts import render
from cursos.models import Curso

def paginaPrincipal(request):
    return render(request, 'inicio/principal.html')

def Cursos(request):
    return render(request, 'inicio/cursos.html')

def Contacto(request):
    cursos = Curso.objects.filter(activo=True)
    return render(request, 'inicio/contacto.html', {'cursos': cursos})

