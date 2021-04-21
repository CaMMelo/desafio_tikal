import re

from django.core.exceptions import ValidationError


def validate_cpf(cpf):
    if len(cpf) < 11:
        raise ValidationError("cpf inválido")
    d1 = sum([(int(d) * (9 - (i % 10))) for i, d in enumerate(cpf[8::-1])]) % 11 % 10
    if d1 != int(cpf[9]):
        raise ValidationError("cpf inválido")
    d2 = sum([(int(d) * (9 - (i % 10))) for i, d in enumerate(cpf[9::-1])]) % 11 % 10
    if d2 != int(cpf[10]):
        raise ValidationError("cpf inválido")


def validate_ddd(ddd):
    if not re.search("^[0-9]{2}$", ddd):
        raise ValidationError("ddd inválido")


def validate_numero(numero):
    if not re.search("^[0-9]{8}$", numero):
        raise ValidationError("numero inválido")
