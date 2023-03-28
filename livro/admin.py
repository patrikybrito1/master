from django.contrib import admin
from .models import Livros, Categoria, Turma, Emprestimos
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
class SearchBook(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(Categoria, SearchBook)
admin.site.register(Livros, SearchBook)
admin.site.register(Emprestimos)
admin.site.register(Turma)
