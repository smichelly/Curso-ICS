from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
