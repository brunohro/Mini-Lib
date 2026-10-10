from django.contrib import admin

from .models import Livro, Autor, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'mostrar_autores', 'ano_publicacao', 'disponivel')
    search_fields = ('titulo', 'autores__nome')

    def mostrar_autores(self, obj):
        return ", ".join([autor.nome for autor in obj.autores.all()])
    mostrar_autores.short_description = 'Autores'