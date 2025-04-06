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

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            return redirect('home')  # redireciona para uma página de sucesso
        except Usuario.DoesNotExist:
            return render(request, 'login/home.html', {'error': 'Email ou senha inválidos.'})
    
    return render(request, 'login/home.html') # colocar pra onde vai redirecionar quando der sucesso