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
    tipo_quarto = models.CharField(max_length=150, choices=[
        ('quarto com uma cama de solteiro', 'Quarto com uma cama de solteiro'),
        ('quarto com duas camas de solteiro', 'Quarto com duas camas de solteiro'),
        ('quarto com uma cama de casal', 'Quarto com uma cama de casal'),
        ('quarto com duas cama de casal', 'Quarto com duas cama de casal'),
        ('quarto com uma cama de casal e uma de solteiro', 'Quarto com uma cama de casal e uma de solteiro'),
        ('quarto com duas cama de casal e duas de solteiro', 'Quarto com duas cama de casal e duas de solteiro')

    ],
    default='quarto com uma cama de casal')
    documento = models.CharField(max_length=150)
    checkin = models.DateField(auto_now_add=True)
    checkout = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo


# Create your models here.
