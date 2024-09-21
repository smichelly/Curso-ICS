from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    data_nascimento = models.DateField(max_length=10)
    ativo = models.BooleanField(unique=True)
    
    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100)

    def __str__(self):
        return self.nome
    



