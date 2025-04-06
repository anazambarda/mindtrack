from django.shortcuts import render, redirect
from .models import Usuario
from .forms import CadastroForm

def home(request):
    return render(request, 'login/home.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redireciona para uma página de sucesso
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro/cadastro.html', {'form': form})
