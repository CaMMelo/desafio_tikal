# Generated by Django 3.2 on 2021-04-20 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=80)),
                ("rg", models.CharField(max_length=14, unique=True)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("data_nascimento", models.DateField()),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")],
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Telefone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ddd", models.IntegerField()),
                ("numero", models.CharField(max_length=11, unique=True)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("CE", "Celular"),
                            ("RE", "Residencial"),
                            ("CO", "Comercial"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crud.cliente"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crud.cliente"
                    ),
                ),
            ],
        ),
    ]
