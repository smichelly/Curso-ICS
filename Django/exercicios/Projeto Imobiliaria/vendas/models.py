from django.db import models

class Venda(models.Model):
    imovel = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    quantidade = models.IntegerField()
    descricacao = models.TextField()
    data_venda = models.DateField()
    ativo = models.BooleanField(default=True)
    foto_vendas = models.ImageField(upload_to='vendas', blank=True, null=True)

    def __str__(self):
        return self.imovel

class Reserva(models.Model):
    imovel = models.CharField(max_length=100)
    descricao = models.TextField()
    data_reserva = models.DateField(auto_now=True)

    def __str__(self):
        return self.imovel