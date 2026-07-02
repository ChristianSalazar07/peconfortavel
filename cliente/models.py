from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

# Create your models here.
class cliente(models.Model):
    estados = [
        ("rj","RJ"),
        ("sp","SP"),
        ("mg","MG"),
        ("es","ES"),
        ("pr","PR"),
        ("ba","BA"),
        ("rs","RS"),
    ]
    generos = [
        ("M","Masculino"),
        ("F","Feminino"),
        ("O","Outro"),
    ]
    contatos = [
        ("C","Carta"),
        ("E","E-mail"),
        ("T","Telefone"),
        ("F","Fax"),
    ]
    cpf = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70, null=False, help_text="Informe o nome:")
    endereco = models.CharField(max_length=100, null=False, help_text="Informe o endereço:")
    telefone = models.CharField(max_length=11, null=False, help_text="Informe o Telefone:")
    uf = models.CharField(max_length=2, null=False, help_text="Informe o UF:", choices=estados)
    cidade = models.CharField(max_length=50, null=False, help_text="Informe a cidade:")
    genero = models.CharField(max_length=1, null=False, help_text="Informe o gênero:", choices=generos)
    contato = models.CharField(max_length=1, null=False, help_text="Informe a forma de contato:", choices=contatos)
    email = models.CharField(max_length=100, null=True, help_text="Informe o E-mail:")
    senha = models.CharField(max_length=256, null=False, help_text="Informe a senha:")
    custom_salt = models.CharField(max_length=32, null=False, help_text="Salt gerado")

    def __str__(self):
        return f"CPF: {self.cpf} - Nome: {self.nome} - Telefone: {self.telefone}"
    
    def save(self):
        if not self.senha.startswith(('pbkdf2_', 'argon2', 'bcrypt')):
            self.custom_salt = get_random_string(length=32)
            self.senha = make_password(self.senha, salt=self.custom_salt)
        super().save()
