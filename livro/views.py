from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros, Emprestimos
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator


@csrf_exempt
def home(request):
    if request.session.get('usuario'):
        txt_name = request.GET.get('nome')
        livros = Livros.objects.filter(nome__icontains=txt_name or '')
        livros_paginator = Paginator(livros, 10)
        page_num = request.GET.get('page')
        page = livros_paginator.get_page(page_num)

        emprestimos = Emprestimos.objects.all()


        return render(request, 'home.html', {'page': page, 'emprestimos': emprestimos, 'usuario_logado':request.session.get('usuario')})

    else:
        return redirect('/auth/login/?status=2')

@csrf_exempt
def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        return render(request, 'ver_livro.html', {'livro': livros, 'usuario_logado':request.session.get('usuario')})
    return redirect('/auth/login/?status=2')

def excluir_livro(request, livro_id):
    livro = get_object_or_404(livro, pk=livro_id)
    is_borrowed = livro.esta_emprestado  # verifica se o livro está emprestado

    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')

    return render(request, 'excluir_livro.html', {'livro': livro, 'is_borrowed': is_borrowed})