from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    estoque = models.IntegerField(max_length=100)
    codigo = models.CharField(max_length=100)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome
    
class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome