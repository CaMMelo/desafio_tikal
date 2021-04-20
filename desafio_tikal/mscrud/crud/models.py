from django.db import models

SEXO_CHOICES = (
    ("M", "Masculino"),
    ("F", "Feminino"),
    ("O", "Outro"),
)


class Cliente(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    rg = models.CharField(max_length=14, blank=False, null=False, unique=True)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    data_nascimento = models.DateField(null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False)


TIPO_TELEFONE_CHOICES = (
    ("CE", "Celular"),
    ("RE", "Residencial"),
    ("CO", "Comercial"),
)


class Telefone(models.Model):
    ddd = models.IntegerField(null=False)
    numero = models.CharField(max_length=11, unique=True)
    tipo = models.CharField(max_length=2, choices=TIPO_TELEFONE_CHOICES)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Email(models.Model):
    email = models.EmailField(null=False, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
