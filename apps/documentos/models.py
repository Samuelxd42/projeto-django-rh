from django.db import models


class Documeto(models.Model):
    descricao = models.CharField(max_length=100, help_text='Nome do Documeto')

    def __str__(self):
        return self.descricao
