from django import forms
from .models import cliente

class clienteForm(forms.Form):
    cpf = forms.IntegerField(required=True)
    nome = forms.CharField(max_length=70, required=True, help_text="Informe o nome:")
    endereco = forms.CharField(max_length=100, required=True, help_text="Informe o endereço:")
    telefone = forms.CharField(max_length=11, required=True, help_text="Informe o Telefone:")
    uf = forms.ChoiceField(required=True, help_text="Informe o UF:", choices=cliente.estados)
    cidade = forms.CharField(max_length=50, required=True, help_text="Informe a cidade:")
    genero = forms.ChoiceField(required=True, help_text="Informe o gênero:", choices=cliente.generos)
    contato = forms.ChoiceField(required=True, help_text="Informe a forma de contato:", choices=cliente.contatos)
    email = forms.CharField(max_length=100, required=True, help_text="Informe o E-mail:")
    senha = forms.CharField(max_length=256, required=True, help_text="Informe a senha:")

class loginForm(forms.Form):
    email = forms.CharField(max_length=100, required=True, help_text="Informe o E-mail:")
    senha = forms.CharField(max_length=256, required=True, help_text="Informe a senha:")

class senhaForm(forms.Form):
    senhaAtual = forms.CharField(max_length=100, required=True, help_text="Informe a senha atual:")
    senhaNova = forms.CharField(max_length=256, required=True, help_text="Informe a senha nova:")