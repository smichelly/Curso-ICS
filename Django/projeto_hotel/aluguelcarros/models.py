from django.db import models

class Tipo_carro(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome
    
class Forma_pagamento(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome

class Aluguelcarros(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    tipo_carro = models.ForeignKey(Tipo_carro, on_delete=models.SET_NULL, null=True)
    forma_pagamento = models.ForeignKey(Forma_pagamento, on_delete=models.SET_NULL, null=True)
    inicio_reserva = models.DateField(auto_now_add=True)
    fim_reserva = models.DateField(auto_now_add=True)
    motorista = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.nome


#    data_aluguel = models.DateField(max_length=10)
#    pessoa = models.CharField(max_length=100)
#   veiculo = models.CharField(max_length=100)
#   motorista = models.BooleanField(default=True, null=False)