from django import forms
from fabricante.models import fabricante
from .models import produto

class produtoForm(forms.Form):

    cores_possiveis = produto.cores
    nome = forms.CharField(max_length=70, required=True, help_text="Informe o nome do produto:")
    preco_compra = forms.FloatField(required=True, help_text="Informe o valor de compra:")
    preco_venda = forms.FloatField(required=True, help_text="Informe o valor de venda:")
    cor = forms.ChoiceField(required=True, help_text="Informe a cor do produto:", choices=cores_possiveis)
    imagem = forms.CharField(max_length=25, required=True, help_text="Informe o nome da imagem do produto:")
    fabricante_codigo = forms.ModelChoiceField(queryset=fabricante.objects.all(), required=True ,help_text="Informe o fabricante")