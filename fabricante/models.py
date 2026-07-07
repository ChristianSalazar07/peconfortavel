from django.db import models

# Create your models here.
class fabricante(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70, null=False, blank=False, help_text="Informe o nome do fabricante:")
    desativado = models.BooleanField(default=False)

    def __str__(self):
        return f"Código: {self.codigo} - Nome: {self.nome} {' - Desativado' if self.desativado else ''}"