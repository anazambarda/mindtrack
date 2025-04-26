from django.shortcuts import render, redirect
from .models import Usuario
from .models import Pergunta, Formulario, Resposta, Resultado
from django.contrib import messages
from .forms import CadastroForm
from .models import Usuario
from datetime import date
from django.db.models import Avg, Sum, Min, Max, Count, Q



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
        if pontuacao == 0:
            estratificacao = 'Sem transtorno Mental'
        elif pontuacao <= 7:
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
        request.session['estratificacao'] = estratificacao
        return redirect('resultado')  # redireciona para a página de resultado

    return render(request, 'questoes/questoes.html', {'perguntas': perguntas})


def resultado(request):
    estratificacao = request.session.get('estratificacao')
    if not estratificacao:
        return redirect('home')  # caso alguém tente entrar sem passar pelo fluxo certo

    return render(request, 'resultado/resultado.html', {'estratificacao': estratificacao})


def dashboard(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')

    usuario = Usuario.objects.get(usuarioID=usuario_id)

    # 🧹 Pegando filtros do POST
    data_inicio = request.POST.get('data_inicio')
    data_fim = request.POST.get('data_fim')
    idade_min = request.POST.get('idade_min')
    idade_max = request.POST.get('idade_max')
    sexo = request.POST.get('sexo')

    historico_resultados = Resultado.objects.filter(usuario=usuario).order_by('-formulario__data_resposta')

    # 🎯 Aplicar filtros no histórico do usuário
    if data_inicio:
        historico_resultados = historico_resultados.filter(formulario__data_resposta__gte=data_inicio)
    if data_fim:
        historico_resultados = historico_resultados.filter(formulario__data_resposta__lte=data_fim)

    # 🎯 Aplicar filtros de idade e sexo no usuário
    usuarios_filtrados = Usuario.objects.all()

    if idade_min:
        usuarios_filtrados = usuarios_filtrados.filter(idade__gte=idade_min)
    if idade_max:
        usuarios_filtrados = usuarios_filtrados.filter(idade__lte=idade_max)
    if sexo:
        usuarios_filtrados = usuarios_filtrados.filter(sexo=sexo)

    total_usuarios = usuarios_filtrados.count()

    # 🎯 Métricas gerais considerando filtros
    resultados_filtrados = Resultado.objects.filter(usuario__in=usuarios_filtrados)

    if data_inicio:
        resultados_filtrados = resultados_filtrados.filter(formulario__data_resposta__gte=data_inicio)
    if data_fim:
        resultados_filtrados = resultados_filtrados.filter(formulario__data_resposta__lte=data_fim)

    total_resultados = resultados_filtrados.count()

    if total_resultados > 0:
        media_pontuacao_geral = resultados_filtrados.aggregate(media=Avg('pontuacao'))['media'] or 0
        percentual_transtorno = resultados_filtrados.filter(
            ~Q(estratificacao='Sem transtorno Mental')
        ).count() / total_resultados * 100
    else:
        media_pontuacao_geral = 0
        percentual_transtorno = 0

    # 🧮 Métricas individuais (usuário específico)
    total_pontuacao_usuario = historico_resultados.aggregate(total=Sum('pontuacao'))['total'] or 0
    media_pontuacao_usuario = historico_resultados.aggregate(media=Avg('pontuacao'))['media'] or 0

    respostas_sem_transtorno = historico_resultados.filter(estratificacao='Sem transtorno Mental').count()
    respostas_com_transtorno = historico_resultados.exclude(estratificacao='Sem transtorno Mental').count()

    if media_pontuacao_usuario == 0:
        interpretacao_usuario = "Nenhum indício de transtorno mental."
    elif media_pontuacao_usuario <= 7:
        interpretacao_usuario = "Possível transtorno leve."
    elif media_pontuacao_usuario <= 14:
        interpretacao_usuario = "Possível transtorno moderado."
    else:
        interpretacao_usuario = "Possível transtorno grave. Recomendado buscar apoio."

    context = {
        'usuario': usuario,
        'historico_resultados': historico_resultados,
        'total_pontuacao_usuario': total_pontuacao_usuario,
        'media_pontuacao_usuario': round(media_pontuacao_usuario, 2),
        'media_pontuacao_geral': round(media_pontuacao_geral, 2),
        'percentual_transtorno': round(percentual_transtorno, 2),
        'total_usuarios': total_usuarios,
        'idade_min': idade_min,
        'idade_max': idade_max,
        'respostas_sem_transtorno': respostas_sem_transtorno,
        'respostas_com_transtorno': respostas_com_transtorno,
        'interpretacao_usuario': interpretacao_usuario,
        'filtros': {
            'data_inicio': data_inicio,
            'data_fim': data_fim,
            'idade_min': idade_min,
            'idade_max': idade_max,
            'sexo': sexo,
        },
    }

    return render(request, 'dashboard/dashboard.html', context)
