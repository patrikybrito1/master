from django.contrib import admin
from .models import Livros, Categoria, Turma, Emprestimos

@admin.register(Emprestimos)
class EmprestimosAdmin (admin.ModelAdmin):
    readonly_fields =  (["tempo_duracao"])
class SearchBook(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(Categoria, SearchBook)
admin.site.register(Livros, SearchBook)
admin.site.register(Turma)
