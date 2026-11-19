from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    LivroListView,
    AutorDetailView,
    AutorCreateView,
    LivroCreateView,
    LivroUpdateView,
    LivroDeleteView,
    SobreView,
)
    

urlpatterns = [
    path('', LivroListView.as_view(), name='listar_livros'),
    path('autores/<int:id>/', AutorDetailView.as_view(), name='autor'),

    path('autores/cadastro/', AutorCreateView.as_view(), name='cadastro_autor'),

    path('livros/novo/', LivroCreateView.as_view(), name='novo_livro'),
    path('livros/<int:livro_id>/editar/', LivroUpdateView.as_view(), name='editar_livro'),
    path('livros/<int:livro_id>/excluir/', LivroDeleteView.as_view(), name='excluir_livro'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)