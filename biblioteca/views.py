from django.shortcuts import get_object_or_404, redirect, render
from .models import Livro, Autor
from .forms import AutorForm, LivroForm
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy, reverse

#listar livros
class LivroListView(ListView):
    model = Livro
    template_name = 'biblioteca/listar_livros.html'
    context_object_name = 'livros'
    ordering = ['titulo']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autores'] = Autor.objects.all()
        return context

#detalhes do autor
class AutorDetailView(DetailView):
    model = Autor
    template_name = 'biblioteca/autor.html'
    context_object_name = 'autor'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livros'] = self.object.livros.all()
        return context

#cadastrar autor
class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/cadastro_autor.html'
    success_url = reverse_lazy('listar_livros')

#cadastrar livro
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/forms/form_livros.html'
    success_url = reverse_lazy('listar_livros')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo_pagina'] = 'Novo livro'
        contexto['texto_botao'] = 'Cadastrar livro'
        return contexto

    def get_success_url(self):
        if self.object.autores.exists():
            return reverse('autor', kwargs={
                'id': self.object.autores.first().id
            })
        return super().get_success_url()

#editar livro
class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/forms/form_livros.html'
    context_object_name = 'livro'
    pk_url_kwarg = 'livro_id'
    success_url = reverse_lazy('listar_livros')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo_pagina'] = 'Editar livro'
        contexto['texto_botao'] = 'Salvar alterações'
        return contexto

    def get_success_url(self):
        if self.object.autores.exists():
            return reverse('autor', kwargs={
                'id': self.object.autores.first().id
            })
        return super().get_success_url()

#deletar livro
class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'biblioteca/livro_confirm_delete.html'
    context_object_name = 'livro'
    pk_url_kwarg = 'livro_id'
    success_url = reverse_lazy('listar_livros')

#sobre 
class SobreView(TemplateView):
    template_name = 'biblioteca/sobre.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['total_livros'] = Livro.objects.count()
        contexto['livros_disponiveis'] = Livro.objects.filter(
            disponivel=True
        ).count()

        return contexto

