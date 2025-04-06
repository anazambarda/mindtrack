# scripts/inserir_perguntas.py
from projeto_mindtrack.models import Pergunta

perguntas = [
    'Você tem dores de cabeça frequentes?',
    'Tem falta de apetite?',
    'Dorme mal?',
    'Assusta-se com facilidade?',
    'Tem tremores nas mãos?',
    'Sente-se nervoso(a), tenso(a) ou preocupado(a)?',
    'Tem má digestão?',
    'Tem dificuldades de pensar com clareza?',
    'Tem se sentido triste ultimamente?',
    'Tem chorado mais do que de costume?',
    'Encontra dificuldades para realizar com satisfação suas atividades diárias?',
    'Tem dificuldades para tomar decisões?',
    'Tem dificuldades no serviço (seu trabalho é penoso, causa-lhe sofrimento?)',
    'É incapaz de desempenhar um papel útil em sua vida?',
    'Tem perdido o interesse pelas coisas?',
    'Você se sente uma pessoa inútil, sem préstimo?',
    'Tem tido ideia de acabar com a vida?',
    'Sente-se cansado(a) o tempo todo?',
    'Você se cansa com facilidade?',
    'Tem sensações desagradáveis no estômago?',
]

for idx, texto in enumerate(perguntas, start=1):
    Pergunta.objects.get_or_create(perguntaID=idx, pergunta=texto)

print("Perguntas inseridas com sucesso.")
