from django.db import models

class Cadastro(models.Model):
    nome_completo = models.CharField(max_length= 150)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=1000)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=150, choices=[
        ('cpf','CPF'),
        ('rg','RG'),
        ('cn','CN'),
        ('passaporte','PASSAPORTE'),
        ('cie','CIE'),
        ('ci','CI'),
        ('dni','DNI'),

    ],
    default='cpf')
    documento = models.CharField(max_length=150)
    checkin = models.DateField(auto_now_add=True)
    checkout = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo


# Create your models here.
