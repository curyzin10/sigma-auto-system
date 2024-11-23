from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ..forms.veiculo_form import VeiculoForm
from ..models import Veiculo


# Listar todos os clientes
@login_required  # Apenas usuários autenticados poderão acessar
def veiculo_list(request):
    # Ordenar os veículos por marca e modelo
    veiculos = Veiculo.objects.order_by('marca', 'modelo')
    return render(request, 'veiculo/veiculo_page.html', {'veiculos': veiculos, 'model_name': 'veiculos'})


# Exibir o formulário para criar um novo cliente
@login_required  # Apenas usuários autenticados poderão acessar
def veiculo_create(request):
    cancel_url = 'veiculo_page'
    if request.method == 'POST':

        form = VeiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('veiculo_page')
    else:
        form = VeiculoForm()
    return render(request, 'generic_form.html', {'form': form, 'action': 'create',
                                                 'cancel_url': cancel_url, })


# Exibir o formulário para editar um cliente existente
@login_required  # Apenas usuários autenticados poderão acessar
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
@login_required  # Apenas usuários autenticados poderão acessar
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

@login_required  # Apenas usuários autenticados poderão acessar
def veiculo_detalhes(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, 'veiculo/veiculo_detalhes.html', {'veiculo': veiculo})
