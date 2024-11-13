from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404, redirect

from ..forms.operaca_venda_form import OperacaoDeVendaForm
from ..models import OperacaoDeVenda


# Listar todos os clientes
def operacao_venda_list(request):
    operacoes_venda = OperacaoDeVenda.objects.all()
    print(operacoes_venda)
    print("aqqqui")
    return render(request, 'operacoes/operacao_venda.html', {'operacoes_venda': operacoes_venda})


# Exibir o formulário para criar um novo cliente
def operacao_venda_create(request):
    cancel_url = 'operacao_venda'
    if request.method == 'POST':
        form = OperacaoDeVendaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect('operacao_venda')

    else:
        form = OperacaoDeVendaForm()
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'create', 'cancel_url': cancel_url, 'model_name': 'Operação de venda'})


# Exibir o formulário para editar um cliente existente
def operacao_venda_update(request, pk):
    cancel_url = 'operacao_venda'
    operacao_venda = get_object_or_404(OperacaoDeVenda, pk=pk)

    if request.method == 'POST':
        form = OperacaoDeVendaForm(request.POST, instance=operacao_venda)
        if form.is_valid():
            form.save()
            return redirect('operacao_venda')  # Redireciona para a lista de clientes
    else:
        form = OperacaoDeVendaForm(instance=operacao_venda)
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'update', 'operacao_venda': operacao_venda, 'cancel_url': cancel_url, })


# Deletar um cliente
def operacao_venda_delete(request, pk):
    operacao_venda = get_object_or_404(OperacaoDeVenda, pk=pk)

    # Definir parâmetros dinâmicos
    item_name = 'operacao_venda'
    item_value = operacao_venda.numero
    cancel_url = 'operacao_venda'  # URL para voltar à lista de clientes

    if request.method == 'POST':
        operacao_venda.delete()
        return redirect('operacao_venda')  # Redirecionar para a lista de clientes

    return render(request, 'confirm_delete.html', {
        'item_name': item_name,
        'item_value': item_value,
        'cancel_url': cancel_url,
    })
