from django.shortcuts import render, get_object_or_404, redirect

from ..forms.vendedor_form import VendedorForm
from ..models import Vendedor


# Listar todos os clientes
def vendedor_list(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor/vendedor_list.html', {'vendedores': vendedores, 'model_name': 'vendedores'})


# Exibir o formulário para criar um novo cliente
def vendedor_create(request):
    cancel_url = 'vendedor_list'
    if request.method == 'POST':

        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')  # Redireciona para a lista de clientes
    else:
        form = VendedorForm()
    return render(request, 'generic_form.html', {'form': form, 'action': 'create',
                                                 'cancel_url': cancel_url, })


# Exibir o formulário para editar um cliente existente
def vendedor_update(request, pk):
    cancel_url = 'vendedor_list'
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')  # Redireciona para a lista de clientes
    else:
        form = VendedorForm(instance=vendedor)
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'update', 'vendedor': vendedor, 'cancel_url': cancel_url, })


# Deletar um cliente
def vendedor_delete(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)

    # Definir parâmetros dinâmicos
    item_name = 'vendedor'
    item_value = f"{vendedor.marca}, {vendedor.modelo}, {vendedor.placa}"
    cancel_url = 'vendedor_list'  # URL para voltar à lista de clientes

    if request.method == 'POST':
        vendedor.delete()
        return redirect('vendedor_list')  # Redirecionar para a lista de clientes

    return render(request, 'confirm_delete.html', {
        'item_name': item_name,
        'item_value': item_value,
        'cancel_url': cancel_url,
    })
