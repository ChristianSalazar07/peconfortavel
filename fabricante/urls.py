from django.urls import path
from . import views

app_name = "fabricante"

urlpatterns = [
    path('listar/', views.listar, name='listar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigoFabricante>', views.excluir, name="excluir"),
    path('atualizar/<int:codigoFabricante>', views.atualizar, name="atualizar")
]