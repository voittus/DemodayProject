from django.db import models
from django import forms
# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=140)
    email = models.EmailField()
    senha = models.CharField(max_length=140)
    def __str__(self):
        return self.nome

class Alagou(models.Model):
    bairro = models.CharField(max_length=200)
    situacao = models.CharField(max_length=300)
    trafego = models.CharField(max_length=150)
    def __str__(self):
        return self.bairro