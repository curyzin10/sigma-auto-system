from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ..forms.operacao_compra_form import OperacaoDeCompraForm
from ..models import OperacaoDeCompra


# Listar todos os clientes
@login_required  # Apenas usuários autenticados poderão acessar
def operacao_compra_list(request):
    operacoes_compra = OperacaoDeCompra.objects.all()
    return render(request, 'operacoes/operacao_compra.html', {'operacoes_compra': operacoes_compra})


# Exibir o formulário para criar um novo cliente
@login_required  # Apenas usuários autenticados poderão acessar
def operacao_compra_create(request):
    cancel_url = 'operacao_compra'
    if request.method == 'POST':
        form = OperacaoDeCompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operacao_compra')  # Redireciona para a lista de clientes
    else:
        form = OperacaoDeCompraForm()
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'create', 'cancel_url': cancel_url, 'model_name': 'Operação de compra'})


# Exibir o formulário para editar um cliente existente
@login_required  # Apenas usuários autenticados poderão acessar
def operacao_compra_update(request, pk):
    cancel_url = 'operacao_compra'
    operacao_compra = get_object_or_404(OperacaoDeCompra, pk=pk)
    print(operacao_compra.valor)
    if request.method == 'POST':
        form = OperacaoDeCompraForm(request.POST, instance=operacao_compra)
        if form.is_valid():
            form.save()
            return redirect('operacao_compra')  # Redireciona para a lista de clientes
    else:
        form = OperacaoDeCompraForm(instance=operacao_compra)
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'update', 'operacao_compra': operacao_compra, 'cancel_url': cancel_url, })


# Deletar um cliente
@login_required  # Apenas usuários autenticados poderão acessar
def operacao_compra_delete(request, pk):
    operacao_compra = get_object_or_404(OperacaoDeCompra, pk=pk)

    # Definir parâmetros dinâmicos
    item_name = 'operacao_compra'
    item_value = operacao_compra.numero
    cancel_url = 'operacao_compra'  # URL para voltar à lista de clientes

    if request.method == 'POST':
        operacao_compra.delete()
        return redirect('operacao_compra')  # Redirecionar para a lista de clientes

    return render(request, 'confirm_delete.html', {
        'item_name': item_name,
        'item_value': item_value,
        'cancel_url': cancel_url,
    })
