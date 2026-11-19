from django.urls import path
from .views import listar_livros, autor, cadastro_autor, cadastrar_editar_livro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', listar_livros, name='listar_livros'),
    path('autores/<int:id>/', autor, name='autor'),

    path('autores/cadastro/', cadastro_autor, name='cadastro_autor'),

    path('livros/novo/', cadastrar_editar_livro, name='novo_livro'),
    path('livros/<int:livro_id>/editar/', cadastrar_editar_livro, name='editar_livro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)