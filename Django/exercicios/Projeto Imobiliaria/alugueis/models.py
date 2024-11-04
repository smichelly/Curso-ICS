from django.db import models

class ImovelAluguel(models.Model):
    alugar = models.CharField(max_length=100)
    preco_mes = models.DecimalField(decimal_places=2, max_digits=8)
    descricacao = models.TextField()
    endereco = models.CharField(max_length=100)
    disponibilidade_inicio = models.DateField()
    disponibilidade_fim = models.DateField()
    ativo = models.BooleanField(default=True)
    foto_imovelaluguel = models.ImageField(upload_to='alugueis', blank=True, null=True)

    def __str__(self):
        return self.alugar
    
class Contrato(models.Model):
    imovel = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    nome_cliente = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_cliente

    
