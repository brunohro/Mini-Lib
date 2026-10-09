from django.urls import path
from .views import listar_livros, autor

urlpatterns = [
    path('', listar_livros, name='listar_livros'),
    path('autores/<int:id>/', autor, name='autor'),
]
