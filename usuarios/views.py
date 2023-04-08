
from django.shortcuts import redirect, render
from django. http import HttpResponse
from .models import Usuario
from hashlib import sha256
from .models import Turma
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

@csrf_exempt
def cadastro(request):
    status = request.GET.get('status')
    turmas = Turma.objects.all()
    return render(request, 'cadastro.html', {'status': status, 'turmas': turmas})

@csrf_exempt
def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    turma = request.POST.get('turma')
    telefone = request.POST.get('telefone')

    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome,
                          senha=senha,
                          email=email,
                          telefone = telefone,
                          )
        if turma:
            usuario.turma = Turma.objects.get(id=turma)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

@csrf_exempt
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect('/auth/login?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/livro/home')

    return HttpResponse(f"{email}, {senha}")


def sair(request):
    request.session.flush()
    return redirect('/auth/login/')


def turma(request):
    results = Usuario.objects.all()
    return render(request, "cadastro.html", {"turma": results})


