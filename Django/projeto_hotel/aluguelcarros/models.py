from django.db import models


class Carros(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='Carros', blank=True, null=True)

    def __str__(self):
        return self.nome    

class Aluguelcarros(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    forma_pagamento = models.CharField(max_length=150)
    inicio_reserva = models.DateField(auto_now_add=False, help_text='Data de inicio da reserva')
    fim_reserva = models.DateField(auto_now_add=False)
    carro = models.ForeignKey(Carros, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome + " - " + self.cpf
