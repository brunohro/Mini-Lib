from django.shortcuts import get_object_or_404, render
from .models import Livro, Autor

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})

def autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    livros = autor.books.all()
    return render(request, 'biblioteca/autor.html', {'autor': autor, 'livros': livros})