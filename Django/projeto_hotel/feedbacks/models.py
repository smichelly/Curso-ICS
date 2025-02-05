from django.db import models

class Feedback(models.Model):
    opiniao = models.TextField(max_length=999)
    classificar = models.IntegerField()

    def __str__(self):
        return self.opiniao
    

