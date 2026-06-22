from django.shortcuts import render
from .models import cliente
from .forms import clienteForm

# Create your views here.
def listar(request):
    lista_clientes = cliente.objects.all()
    context = {
        "clientes": lista_clientes
    }
    return render(request, 'cliente/listar_clientes.html', context)

def cadastrar(request):
    lista_estados = cliente.estados
    lista_generos = cliente.generos
    lista_contatos = cliente.contatos
    context = {
        "ufs": lista_estados,
        "generos": lista_generos,
        "contatos": lista_contatos
    }
    form = clienteForm(request.POST)
    if form.is_valid():
        dados_cliente = form.cleaned_data
        c = cliente(
            cpf = dados_cliente['cpf'],
            nome = dados_cliente['nome'],
            endereco = dados_cliente['endereco'],
            telefone = dados_cliente['telefone'],
            uf = dados_cliente['uf'],
            cidade = dados_cliente['cidade'],
            genero = dados_cliente['genero'],
            contato = dados_cliente['contato'],
            email = dados_cliente['email'],
            senha = dados_cliente['senha'],
        )
        c.save()
    return render(request, 'cliente/cadastrar_clientes.html', context)