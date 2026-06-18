from django.db import models

# Create your models here.
class cliente(models.Model):
    cpf = models.IntegerField(primary_key=True, max_length=11)
    nome = models.CharField(max_length=70, null=False, help_text="Informe o nome:")
    endereco = models.CharField(max_length=100, null=False, help_text="Informe o endereço:")
    telefone = models.IntegerField(null=False, help_text="Informe o Telefone:")
    uf = models.CharField(max_length=2, null=False, help_text="Informe o UF:")
    cidade = models.CharField(max_length=50, null=False, help_text="Informe a cidade:")
    genero = models.CharField(max_length=1, null=False, help_text="Informe o gênero:")
    contato = models.CharField(max_length=1, null=False, help_text="Informe a forma de contato:")
    email = models.CharField(max_length=100, null=True, help_text="Informe o E-mail:")
    senha = models.CharField(max_length=256, null=False, help_text="Informe o E-mail:")

    def __str__(self):
        return f"CPF: {self.cpf} - Nome: {self.nome} - Telefone: {self.telefone}"