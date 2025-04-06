from django.db import models

class usuario(models.Model):
    usuarioID = models.AutoField(primary_key = True)
    nome = models.TextField(max_length = 255)
    email = models.TextField(max_length = 255)
    senha = models.TextField(max_length = 255)
    idade = models.IntegerField()
    sexo = models.TextField(max_length = 20)
