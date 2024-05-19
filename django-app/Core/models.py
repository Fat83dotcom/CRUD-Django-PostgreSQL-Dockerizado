from django.db import models


class CadastroCliente(models.Model):
    nome = models.CharField(max_length=512, blank=True)
    email = models.EmailField(max_length=512, blank=False, unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cidade = models.CharField(max_length=512, blank=True)

    def __str__(self) -> str:
        return self.nome
