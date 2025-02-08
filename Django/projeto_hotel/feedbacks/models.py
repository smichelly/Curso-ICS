from django.db import models

class Feedback(models.Model):
    comentario = models.TextField(max_length=999)
    classificar = models.CharField(max_length=150, choices=[
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),

    ],
    default='0')

    def __str__(self):
        return self.comentario
    

