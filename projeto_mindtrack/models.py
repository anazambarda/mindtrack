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
