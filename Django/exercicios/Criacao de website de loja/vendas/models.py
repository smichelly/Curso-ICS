from django.db import models

class Venda(models.Model):
    data =  models.DateTimeField(max_length=10)
    valor_total =  models.DecimalField(decimal_places=2, max_digits=8)
    forma_pagamento = models.CharField(max_length=50)
    observacao = models.TextField(max_length=100)

    def _str_(self):
        return self.data
    

class Cobranca(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=8)
    status = models.CharField(max_length=100)
    data_vencimento = models.DateField(max_length=10)
    data_pagamento = models.DateField(max_length=10)
    metodo = models.CharField(max_length=100)

    def _str_(self):
        return self.status
    
class Entrega(models.Model):
    endereco_entrega = models.CharField(max_length=100)
    data_envio = models.DateTimeField(max_length=100)
    data_entrega = models.DateTimeField(max_length=100)
    status = models.CharField(max_length=100)
    codigo_rastreamento = models.CharField(max_length=100)

    def _str_(self):
        return self.endereco_entrega


