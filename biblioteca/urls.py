from django.urls import path
from .views import listar_livros, autor, cadastro_autor

urlpatterns = [
    path('', listar_livros, name='listar_livros'),
    path('autores/<int:id>/', autor, name='autor'),

    path('autores/cadastro/', cadastro_autor, name='cadastro_autor'),
]
