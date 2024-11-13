from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404, redirect

from ..forms.fazer_pedido_form import FazerPedidoForm
from ..models import Pedido


# Listar todos os clientes
def fazer_pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'operacoes/fazer_pedido.html', {'pedidos': pedidos})


# Exibir o formulário para criar um novo cliente
def fazer_pedido_create(request):
    cancel_url = 'fazer_pedido'
    if request.method == 'POST':
        form = FazerPedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fazer_pedido')

    else:
        form = FazerPedidoForm()
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'create', 'cancel_url': cancel_url, 'model_name': 'fazer_pedido'})


# Exibir o formulário para editar um cliente existente
def fazer_pedido_update(request, pk):
    cancel_url = 'fazer_pedido'
    pedido = get_object_or_404(Pedido, pk=pk)

    if request.method == 'POST':
        form = FazerPedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('fazer_pedido')  # Redireciona para a lista de clientes
    else:
        form = FazerPedidoForm(instance=pedido)
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'update', 'pedido': pedido, 'cancel_url': cancel_url, })


# Deletar um cliente
def fazer_pedido_delete(request, pk):
    operacao_venda = get_object_or_404(Pedido, pk=pk)

    # Definir parâmetros dinâmicos
    item_name = 'fazer_pedido'
    item_value = operacao_venda.numero
    cancel_url = 'fazer_pedido'  # URL para voltar à lista de clientes

    if request.method == 'POST':
        operacao_venda.delete()
        return redirect('fazer_pedido')  # Redirecionar para a lista de clientes

    return render(request, 'confirm_delete.html', {
        'item_name': item_name,
        'item_value': item_value,
        'cancel_url': cancel_url,
    })
