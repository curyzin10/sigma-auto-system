from django.shortcuts import render, get_object_or_404, redirect
from ..models import Veiculo
from ..forms.veiculo_form import VeiculoForm
from django.urls import reverse


# Listar todos os clientes
def veiculo_list(request):
    # Ordenar os veículos por marca e modelo
    veiculos = Veiculo.objects.order_by('marca', 'modelo')
    return render(request, 'veiculo/veiculo_page.html', {'veiculos': veiculos, 'model_name': 'veiculos'})


# Exibir o formulário para criar um novo cliente
def veiculo_create(request):
    cancel_url = 'veiculo_page'
    if request.method == 'POST':

        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculo_page')  # Redireciona para a lista de clientes
    else:
        form = VeiculoForm()
    return render(request, 'generic_form.html', {'form': form, 'action': 'create',
                                                 'cancel_url': cancel_url, })


# Exibir o formulário para editar um cliente existente
def veiculo_update(request, pk):
    cancel_url = 'veiculo_page'
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('veiculo_page')  # Redireciona para a lista de clientes
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'update', 'veiculo': veiculo, 'cancel_url': cancel_url, })


# Deletar um cliente
def veiculo_delete(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)

    # Definir parâmetros dinâmicos
    item_name = 'veiculo'
    item_value = f"{veiculo.marca}, {veiculo.modelo}, {veiculo.placa}"
    cancel_url = 'veiculo_page'  # URL para voltar à lista de clientes

    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculo_page')  # Redirecionar para a lista de clientes

    return render(request, 'confirm_delete.html', {
        'item_name': item_name,
        'item_value': item_value,
        'cancel_url': cancel_url,
    })
