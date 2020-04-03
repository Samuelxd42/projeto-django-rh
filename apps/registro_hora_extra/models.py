from django.db import models


class RegistroHora(models.Model):
    motivo = models.CharField(max_length=100, help_text='Informe o motivo')

    def __str__(self):
        return self.motivo

