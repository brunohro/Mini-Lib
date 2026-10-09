from django.contrib import admin
from .models import Livro, Autor, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class LivroInline(admin.TabularInline):
    model = Livro  # OBRIGATÓRIO: O Django precisa saber qual modelo este inline edita
    fields = ('titulo', 'categoria', 'autor', 'data_publicacao') 
 

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome',)
    inlines = [LivroInline]