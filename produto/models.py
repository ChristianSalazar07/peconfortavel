from django.db import models
from fabricante.models import fabricante

# Create your models here.
class produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70, null=False, blank=False, help_text="Informe o nome do produto:")
    preco_compra = models.FloatField(null=False, blank=False, help_text="Informe o valor de compra:")
    preco_venda = models.FloatField(null=False, blank=False, help_text="Informe o valor de venda:")
    cor = models.CharField(max_length=70, null=False, blank=False, help_text="Informe o nome do produto:")
    imagem = models.CharField(max_length=70, null=False, blank=False, help_text="Informe o nome do produto:")
    fabricante_codigo = models.ForeignKey(fabricante, on_delete=models.SET_NULL, null=True ,help_text="Informe o fabricante")