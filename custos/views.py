from django.shortcuts import render, redirect
from .models import Cost
from .forms import CostForm
import matplotlib.pyplot as plt
import io
import urllib, base64
import pandas as pd

# página de cadastro
def adicionar_custo(request):
    if request.method == "POST":
        form = CostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_custos')
    else:
        form = CostForm()
    
    return render(request, 'custos/form.html', {'form': form})

# página de listagem
def listar_custos(request):
    categoria = request.GET.get('categoria')  # Filtro por categoria
    if categoria:
        custos = Cost.objects.filter(categoria__icontains=categoria)
    else:
        custos = Cost.objects.all()

    return render(request, 'custos/lista.html', {'custos': custos})

# gerar gráfico
def grafico_gastos(request):
    custos = Cost.objects.all().values()
    if not custos:
        return render(request, 'custos/grafico.html', {'grafico': None})
    
    df = pd.DataFrame(custos)
    df['data'] = pd.to_datetime(df['data'])
    df['mes'] = df['data'].dt.strftime('%m')

    grafico = gerar_grafico(df)

    return render(request, 'custos/grafico.html', {'grafico': grafico})

# função para gerar o gráfico com agrupamento por categoria
def gerar_grafico(df):

    df_grouped = df.groupby(['mes', 'categoria'])['valor'].sum().unstack()

    ax = df_grouped.plot(kind='bar', stacked=True, figsize=(6, 6), colormap='tab10')
    plt.xlabel('Mês')
    plt.ylabel('Total Gasto (R$)')
    plt.title('Gastos Mensais')
    plt.xticks(rotation=45)
    plt.legend(title="Categoria", bbox_to_anchor=(1, 1), loc='upper left')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    grafico = base64.b64encode(image_png).decode('utf-8')
    return f"data:image/png;base64,{grafico}"
