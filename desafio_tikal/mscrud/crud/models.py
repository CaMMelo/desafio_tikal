from django.db import models

from . import validators

SEXO_CHOICES = (
    ("M", "Masculino"),
    ("F", "Feminino"),
    ("O", "Outro"),
)


class Cliente(models.Model):
    class Meta:
        db_table = "crud_cliente"

    nome = models.CharField(max_length=80, blank=False, null=False)
    rg = models.CharField(max_length=14, blank=False, null=False, unique=True)
    cpf = models.CharField(
        max_length=11,
        blank=False,
        null=False,
        unique=True,
        validators=[validators.validate_cpf],
    )
    data_nascimento = models.DateField(null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False)


TIPO_TELEFONE_CHOICES = (
    ("CE", "Celular"),
    ("RE", "Residencial"),
    ("CO", "Comercial"),
)


class Telefone(models.Model):
    class Meta:
        db_table = "crud_telefone"

    ddd = models.CharField(
        max_length=2, null=False, validators=[validators.validate_ddd]
    )
    numero = models.CharField(
        max_length=8, unique=True, validators=[validators.validate_numero]
    )
    tipo = models.CharField(max_length=2, choices=TIPO_TELEFONE_CHOICES)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Email(models.Model):
    class Meta:
        db_table = "crud_email"

    email = models.EmailField(null=False, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
