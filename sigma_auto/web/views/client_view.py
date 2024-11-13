from django.shortcuts import render, get_object_or_404, redirect
from ..models import Cliente
from ..forms.client_form import ClienteForm
from django.urls import reverse


# Listar todos os clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})


# Exibir o formulário para criar um novo cliente
def cliente_create(request):
    cancel_url = 'cliente_list'
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')  # Redireciona para a lista de clientes
    else:
        form = ClienteForm()
    return render(request, 'generic_form.html', {'form': form, 'action': 'create', 'cancel_url': cancel_url, })


# Exibir o formulário para editar um cliente existente
def cliente_update(request, pk):
    cancel_url = 'cliente_list'
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')  # Redireciona para a lista de clientes
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'update', 'cliente': cliente, 'cancel_url': cancel_url, })


# Deletar um cliente
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    # Definir parâmetros dinâmicos
    item_name = 'cliente'
    item_value = cliente.nome
    cancel_url = 'cliente_list'  # URL para voltar à lista de clientes

    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')  # Redirecionar para a lista de clientes

    return render(request, 'confirm_delete.html', {
        'item_name': item_name,
        'item_value': item_value,
        'cancel_url': cancel_url,
    })
