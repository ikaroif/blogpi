from django.shortcuts import render
from .models import Curso, Interesse

def index(request):
    cursos = Curso.objects.all()
    interesses = Interesse.objects.all()
    return render(request, 'blog/index.html', {'cursos': cursos, 'interesses': interesses})

def sobre(request):
    return render(request, 'blog/sobre.html')
