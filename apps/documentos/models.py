from django.db import models
from apps.colaborador.models import Colaborador


class Documeto(models.Model):
    descricao = models.CharField(max_length=100, help_text='Nome do Documeto')
    pertence = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
