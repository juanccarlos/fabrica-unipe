from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rgm = models.CharField(max_length=8)
    data_nascimeno = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nome
