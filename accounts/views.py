from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def register(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirma_senha')
        
        if User.objects.filter(username=nome).exists():
            return HttpResponse('Já existe um usuário com esse nome')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Este email já está sendo usado')

        if senha != confirma_senha:
            return HttpResponse('As senhas não coincidem')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.first_name = nome
        user.last_name = sobrenome
        user.save()

        return HttpResponseRedirect('/login/')

    return render(request, 'register.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)
        print(user)
        
        if user != None:
            login_django(request, user)
            return HttpResponseRedirect('/plataforma/')
        else:
            return HttpResponse('login ou senha inválidos')

def plataforma(request):
    return render(request, 'index.html')

def password(request):
    return render(request, 'password.html')
