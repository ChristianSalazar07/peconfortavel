from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path('listar/', views.listar, name='listar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login')
]