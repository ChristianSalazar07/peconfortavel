from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import produto
from fabricante.models import fabricante
from .forms import produtoForm

# Create your views here.
def listar(request):
    lista_produtos = produto.objects.all()
    context = {
        "produtos": lista_produtos
    }
    return render(request, 'produto/listar_produtos.html', context)

def cadastrar(request):
    lista_fabricantes = fabricante.objects.all()
    lista_cores = produto.cores
    context = {
        "fabricantes": lista_fabricantes,
        "cor": lista_cores
    }
    form = produtoForm(request.POST)
    if form.is_valid():
        dados_produto = form.cleaned_data
        p = produto(
            nome = dados_produto['nome'],
            preco_compra = dados_produto['preco_compra'],
            preco_venda = dados_produto['preco_venda'],
            cor = dados_produto['cor'],
            imagem = dados_produto['imagem'],
            fabricante_codigo = dados_produto['fabricante_codigo'],
        )
        p.save()
    else:
        redirect('produto:listar')
    return render(request, 'produto/cadastrar_produtos.html', context)