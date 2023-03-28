from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    if request.session.get('usuario'):
        txt_name = request.GET.get('nome')
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(nome__icontains=txt_name or '')

        return render(request, 'home.html', {'livros': livros, 'usuario_logado':request.session.get('usuario')})

    else:
        return redirect('/auth/login/?status=2')

@csrf_exempt
def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        return render(request, 'ver_livro.html', {'livro': livros, 'usuario_logado':request.session.get('usuario')})
    return redirect('/auth/login/?status=2')

