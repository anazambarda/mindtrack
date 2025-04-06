from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from .forms import CadastroForm


def home(request):
    return render(request, 'login/home.html')

def cadastro(request):  
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if Usuario.objects.filter(email=email).exists():
                messages.error(request, 'Este email já está em uso.')
                request.session['form_data'] = request.POST
                return redirect('cadastro')  # redireciona mesmo com erro
            else:
                form.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('home')  # redireciona para página de sucesso
    else:
        if 'form_data' in request.session:
            form = CadastroForm(initial=request.session.pop('form_data'))
        else:
            form = CadastroForm()

    return render(request, 'cadastro/cadastro.html', {'form': form})

def perguntas(request):
    return render(request, 'perguntas/perguntas.html')  

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            return redirect('perguntas')
        except Usuario.DoesNotExist:
            request.session['login_erro'] = 'Email ou senha inválidos.'
            request.session['login_email'] = email
            return redirect('login')  

    error = request.session.pop('login_erro', '')
    email = request.session.pop('login_email', '')

    return render(request, 'login/home.html', {'error': error, 'email': email})





# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         senha = request.POST.get('senha')
        
#         try:
#             usuario = Usuario.objects.get(email=email, senha=senha)
#             return redirect('perguntas')  # redireciona para uma página de sucesso
#         except Usuario.DoesNotExist:
#             return render(request, 'login/home.html', {'error': 'Email ou senha inválidos.'})
    
#     return render(request, 'login/home.html') # colocar pra onde vai redirecionar quando der sucesso