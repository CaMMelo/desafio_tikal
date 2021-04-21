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


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Telefone
        fields = [
            "ddd",
            "numero",
            "tipo",
            "cliente",
        ]


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = [
            "email",
            "cliente",
        ]
