from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=70)
    status = models.CharField(max_length=50)
    prazo = models.DateField()

    def __str__(self):
        return self.nome
