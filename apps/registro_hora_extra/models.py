from django.db import models
from apps.colaborador.models import Colaborador


class RegistroHora(models.Model):
    motivo = models.CharField(max_length=100, help_text='Informe o motivo')
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo

