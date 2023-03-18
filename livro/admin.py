from django.contrib import admin
from .models import Livros, Categoria, Turma

class SearchBook(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(Categoria, SearchBook)
admin.site.register(Livros, SearchBook)
admin.site.register(Turma)
