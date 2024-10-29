from __future__ import annotations
from django.contrib.auth.models import AbstractUser
from django.db import models
from usuario.managers import UsuarioManager
from django.templatetags.static import static


class Usuario(AbstractUser):
    username = None
    first_name = None
    last_name = None
    nome_completo = models.CharField(
        "Nome Completo", max_length=100, blank=False, null=False
    )
    email = models.EmailField("E-mail", blank=True, unique=True)
    cpf = models.CharField(max_length=14, unique=True, null=True)  # 123.456.789-09
    telefone = models.CharField(max_length=11, blank=True, null=True)  # (11) 98765-4321
    data_nascimento = models.DateField("Data de  Nascimento", blank=True, null=True)
    matricula = models.CharField(max_length=10, blank=False, null=True) #123456789 - 9 dígitos
    imagem = models.ImageField(
        upload_to="usuario", default=static("usuario/sem_imagem.png")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome_completo"]

    objects = UsuarioManager()

    def __str__(self):
        return self.nome_completo

    def get_primeiro_nome(self):
        return self.nome_completo.split(" ")[0]