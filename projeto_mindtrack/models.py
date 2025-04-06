from django.db import models

class Usuario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    usuarioID = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    senha = models.CharField(max_length = 255)
    idade = models.IntegerField()
    sexo = models.CharField(max_length = 1, choices=SEXO_CHOICES)

class Pergunta(models.Model):
    perguntaID = models.AutoField(primary_key=True)
    pergunta = models.CharField(max_length=255)

    def __str__(self):
        return self.pergunta
    
class Formulario(models.Model):
    formularioID = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    data_resposta = models.DateField(null=True, blank=True)

class Resultado(models.Model):
    resultadoID = models.AutoField(primary_key=True)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    estratificacao = models.CharField(max_length=50)

class FormularioPergunta(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('formulario', 'pergunta')

class Resposta(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.BooleanField()