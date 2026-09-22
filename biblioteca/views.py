from django.shortcuts import render
from .models import Livro

def listar_livros(request):
    livro = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livro})