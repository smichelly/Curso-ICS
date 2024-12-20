from django.db import models

class Tipo_quarto(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome

class Forma_pagamento(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome

class Cadastro(models.Model):
    checkin = models.DateField(auto_now_add=True)
    checkout = models.DateField(auto_now_add=True)
    tipo_quarto = models.ForeignKey(Tipo_quarto, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length= 150)
    telefone = models.IntegerField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    quantidade_pessoas = models.IntegerField()
    forma_pegamento = models.ForeignKey(Forma_pagamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


# Create your models here.
