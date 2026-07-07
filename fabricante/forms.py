from django import forms

class fabricanteForm(forms.Form):
    nome = forms.CharField(max_length=70, required=True, help_text="Informe o nome:")

class atualizarFabricanteForm(forms.Form):
    nome = forms.CharField(max_length=70, required=True, help_text="Informe o nome:")
    codigo = forms.IntegerField(required=True, help_text="Informe o código:")