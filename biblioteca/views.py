from django.shortcuts import get_object_or_404, redirect, render
from .models import Livro, Autor
from .forms import AutorForm, LivroForm

def listar_livros(request):
    livros = Livro.objects.all()
    autores = Autor.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros, 'autores': autores})

def autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    livros = autor.livros.all()
    return render(request, 'biblioteca/autor.html', {'autor': autor, 'livros': livros})

def cadastro_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/cadastro_autor.html', {'form': form})


def cadastrar_editar_livro(request, livro_id=None):
    if livro_id:
        livro = get_object_or_404(Livro, id=livro_id)
    else:
        livro = None

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro_salvo = form.save()

            return redirect(
                'autor',
                id=livro_salvo.autores.first().id
            )

    else:
        form = LivroForm(instance=livro)

    contexto = {
        'form': form,
        'titulo_pagina': 'Editar livro' if livro else 'Novo livro',
        'texto_botao': 'Salvar alterações' if livro else 'Cadastrar livro',
    }

    return render(request, 'biblioteca/forms/form_livros.html', contexto)
