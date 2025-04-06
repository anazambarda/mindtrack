from django.shortcuts import render, redirect
from .models import Usuario
from .forms import CadastroForm

def home(request):
    return render(request, 'login/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoa_sucesso')  # redireciona para uma página de sucesso
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro/cadastro.html', {'form': form})

# def cadastro(request):
#     return render(request, 'cadastro/cadastro.html')

