from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamentos
from apps.empresa.models import Empresa


class Colaborador(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Colaborador')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamentos)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
