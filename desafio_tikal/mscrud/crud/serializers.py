import re

from rest_framework import serializers

from . import models


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = [
            "nome",
            "rg",
            "cpf",
            "data_nascimento",
            "sexo",
        ]

    def validate_cpf(self, cpf):
        d1 = (
            sum([(int(d) * (9 - (i % 10))) for i, d in enumerate(cpf[8::-1])]) % 11 % 10
        )
        if d1 != int(cpf[9]):
            raise serializers.ValidationError("cpf inválido")
        d2 = (
            sum([(int(d) * (9 - (i % 10))) for i, d in enumerate(cpf[9::-1])]) % 11 % 10
        )
        if d2 != int(cpf[10]):
            raise serializers.ValidationError("cpf inválido")
        return cpf


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Telefone
        fields = [
            "ddd",
            "numero",
            "tipo",
            "cliente",
        ]

    def validate_ddd(self, ddd):
        if not re.search("^[0-9]{2}$", ddd):
            raise serializers.ValidationError("numero inválido")
        return ddd

    def validate_numero(self, numero):
        if not re.search("^[9]?[0-9]{8}$", numero):
            raise serializers.ValidationError("numero inválido")
        return numero[:8]


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = [
            "email",
            "cliente",
        ]
