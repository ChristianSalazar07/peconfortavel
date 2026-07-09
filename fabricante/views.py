from django.shortcuts import render, redirect
from .models import fabricante
from .forms import fabricanteForm, atualizarFabricanteForm

# Create your views here.
def listar(request):
    lista_fabricantes = fabricante.objects.filter(desativado=False)
    context = {
        "fabricantes": lista_fabricantes
    }
    return render(request, "fabricante/listar_fabricantes.html", context)

def cadastrar(request):
    form = fabricanteForm(request.POST)
    if form.is_valid():
        dados_fabricante = form.cleaned_data
        fab = fabricante(
            nome = dados_fabricante['nome']
        )
        fab.save()
    return render(request, "fabricante/cadastrar_fabricantes.html")

def excluir(request, codigoFabricante):
    fab = fabricante.objects.get(pk=codigoFabricante)
    fab.desativado = True
    fab.save()
    return redirect("fabricante:listar")

def atualizar(request, codigoFabricante):
    form = atualizarFabricanteForm(request.POST)
    if form.is_valid():
        dados_fabricante = form.cleaned_data
        fab = fabricante.objects.get(pk=dados_fabricante['codigo'])
        fab.nome = dados_fabricante['nome']
        fab.desativado = False
        fab.save()
        return redirect("fabricante:listar")
    context = {
        "codigo": codigoFabricante,
        "fabricanteAlterado": fabricante.objects.get(pk=codigoFabricante)
    }
    return render(request, "fabricante/atualizar_fabricantes.html", context)