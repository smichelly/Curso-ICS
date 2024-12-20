from django.db import models

class Feedback(models.Model):
    opiniao = models.TextField(max_length=999)
    sugestao = models.TextField(max_length=999)
    classificar = models.IntegerField()

    def __str__(self):
        return self.opiniao
    

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField(max_length=999)