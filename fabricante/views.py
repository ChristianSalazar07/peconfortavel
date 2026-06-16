from django.shortcuts import render
from .models import fabricante
from .forms import fabricanteForm

# Create your views here.
def listar(request):
    lista_fabricantes = fabricante.objects.all()
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