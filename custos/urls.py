from django.urls import path
from .views import adicionar_custo, listar_custos, grafico_gastos

urlpatterns = [
    path('novo/', adicionar_custo, name='adicionar_custo'),
    path('', listar_custos, name='listar_custos'),
    path('grafico/', grafico_gastos, name='grafico_gastos'),
]
