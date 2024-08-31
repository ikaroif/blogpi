from django.db import models
from django.utils import timezone

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_conclusao = models.DateField()

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='interesses/', blank=True, null=True)

    def __str__(self):
        return self.titulo
