from django.shortcuts import render
from .models import produto

# Create your views here.
def listar(request):

    return render(request, 'produto/listar_produtos.html')

def cadastrar(request):

    return render(request, 'produto/cadastrar_produtos.html')