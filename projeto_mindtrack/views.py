from django.shortcuts import render, redirect
from .models import Usuario
from .models import Pergunta, Formulario, Resposta, Resultado
from django.contrib import messages
from .forms import CadastroForm
from .models import Usuario
from datetime import date


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
            request.session['usuario_id'] = usuario.usuarioID  # <-- adiciona isso aqui!
            return redirect('perguntas')  # redireciona pro questionário
        except Usuario.DoesNotExist:
            request.session['login_erro'] = 'Email ou senha inválidos.'
            request.session['login_email'] = email
            return redirect('login')  

    error = request.session.pop('login_erro', '')
    email = request.session.pop('login_email', '')

    return render(request, 'login/home.html', {'error': error, 'email': email})


def questoes(request):
    perguntas = Pergunta.objects.all()
    
    if request.method == 'POST':
        usuario_id = request.session.get('usuario_id')
        if not usuario_id:
            return redirect('login') 
        usuario = Usuario.objects.get(usuarioID=usuario_id)
        formulario = Formulario.objects.create(usuario=usuario, data_resposta=date.today())
        pontuacao = 0

        for pergunta in perguntas:
            resposta_str = request.POST.get(f'pergunta_{pergunta.perguntaID}')
            if resposta_str is not None:
                resposta_bool = resposta_str == 'sim'
                if resposta_bool:
                    pontuacao += 1
                Resposta.objects.create(formulario=formulario, pergunta=pergunta, resposta=resposta_bool)

        if pontuacao <= 7:
            estratificacao = 'Transtorno leve'
        elif pontuacao <= 14:
            estratificacao = 'Transtorno moderado'
        else:
            estratificacao = 'Transtorno grave'

        Resultado.objects.create(
            formulario=formulario,
            usuario=usuario,
            pontuacao=pontuacao,
            estratificacao=estratificacao
        )

        return redirect('dashboard/dashboard.html')  # redireciona para a página de resultado

    return render(request, 'questoes/questoes.html', {'perguntas': perguntas})











def dashboard(request):
    return render(request, 'dashboard.html')




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