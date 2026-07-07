from django.urls import path
from . import views

app_name = "produto"

urlpatterns = [
    path('listar/', views.listar, name='listar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigoProduto>', views.excluir, name="excluir"),
    path('atualizar/<int:codigoProduto>', views.atualizar, name="atualizar")
]