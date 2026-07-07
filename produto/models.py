from django.db import models
from fabricante.models import fabricante


# Create your models here.
class produto(models.Model):
    cores = [
    ("azul", "Azul"),
    ("vermelho", "Vermelho"),
    ("verde", "Verde"),
    ("amarelo", "Amarelo"),
    ("branco", "Branco"),
    ("preto", "Preto"),
    ("marrom", "Marrom"),
    ]
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70, null=False, blank=False, help_text="Informe o nome do produto:")
    preco_compra = models.FloatField(null=False, blank=False, help_text="Informe o valor de compra:")
    preco_venda = models.FloatField(null=False, blank=False, help_text="Informe o valor de venda:")
    cor = models.CharField(max_length=20, null=False, blank=False, help_text="Informe a cor do produto:", choices=cores, default="preto")
    imagem = models.CharField(max_length=25, null=False, blank=False, help_text="Informe o nome do produto:")
    fabricante_codigo = models.ForeignKey(fabricante, on_delete=models.SET_NULL, null=True, help_text="Informe o fabricante")
    desativado = models.BooleanField(default=False)

    def __str__(self):
        return f"Código: {self.codigo} - Nome: {self.nome} - Cor: {self.cor.capitalize()} - Fabricante: {self.fabricante_codigo.nome} {' - Desativado' if self.desativado else ''}"