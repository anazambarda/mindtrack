from django.shortcuts import render
from .models import usuario

def home(request):
    return render(request, 'login/home.html')

def usuarios(request):
    novo_usuario = usuario()
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    

def cadastro(request):
    return render(request, 'cadastro/cadastro.html')

