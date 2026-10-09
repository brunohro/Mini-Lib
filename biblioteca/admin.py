from django.contrib import admin

from .models import Livro, Autor, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class LivroInline(admin.TabularInline):
    model = Livro
    fields = ('titulo', 'categoria', 'autor', 'ano_publicacao')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome',)
    inlines = [LivroInline]

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao', 'disponivel')
    search_fields = ('titulo', 'autor__nome')