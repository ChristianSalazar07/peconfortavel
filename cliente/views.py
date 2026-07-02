from django.shortcuts import render
from .models import cliente
from .forms import clienteForm, loginForm
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse

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
        if cliente.objects.filter(email=dados_cliente['email']).exists():
            return HttpResponse("Usuário já existe")
        else:
            c.save()
    return render(request, 'cliente/cadastrar_clientes.html', context)

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            dados_login = form.cleaned_data
            try:
                usuario = cliente.objects.get(email=dados_login['email'])
                p = make_password(dados_login['senha'], salt=usuario.custom_salt)
                if cliente.objects.filter(email=dados_login['email']).exists() and p == usuario.senha:
                    return HttpResponse(f"Sucesso")
                else:
                    mensagem = "Senha incorreta"
                    context = {
                        "mensagem": mensagem
                    }
                    return render(request, 'cliente/login_cliente.html', context)
            except cliente.DoesNotExist:
                mensagem = "Usuário não existente"
                context = {
                    "mensagem": mensagem
                }
                return render(request, 'cliente/login_cliente.html', context)
    return render(request, 'cliente/login_cliente.html')