from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ..forms.montadora_form import MontadoraForm
from ..models import Montadora


# Listar todos os clientes
@login_required  # Apenas usuários autenticados poderão acessar
def montadora_list(request):
    montadoras = Montadora.objects.all()
    return render(request, 'montadora/montadora_list.html', {'montadoras': montadoras})


# Exibir o formulário para criar um novo cliente
@login_required  # Apenas usuários autenticados poderão acessar
def montadora_create(request):
    cancel_url = 'montadora_list'
    if request.method == 'POST':
        form = MontadoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('montadora_list')  # Redireciona para a lista de clientes
    else:
        form = MontadoraForm()
    return render(request, 'generic_form.html', {'form': form, 'action': 'create', 'cancel_url': cancel_url, })


# Exibir o formulário para editar um cliente existente
@login_required  # Apenas usuários autenticados poderão acessar
def montadora_update(request, pk):
    cancel_url = 'montadora_list'
    montadora = get_object_or_404(Montadora, pk=pk)
    if request.method == 'POST':
        form = MontadoraForm(request.POST, instance=montadora)
        if form.is_valid():
            form.save()
            return redirect('montadora_list')  # Redireciona para a lista de clientes
    else:
        form = MontadoraForm(instance=montadora)
    return render(request, 'generic_form.html',
                  {'form': form, 'action': 'update', 'montadora': montadora, 'cancel_url': cancel_url, })


# Deletar um cliente
@login_required  # Apenas usuários autenticados poderão acessar
def montadora_delete(request, pk):
    montadora = get_object_or_404(Montadora, pk=pk)

    # Definir parâmetros dinâmicos
    item_name = 'montadora'
    item_value = montadora.razao_social
    cancel_url = 'montadora_list'  # URL para voltar à lista de clientes

    if request.method == 'POST':
        montadora.delete()
        return redirect('montadora_list')  # Redirecionar para a lista de clientes

    return render(request, 'confirm_delete.html', {
        'item_name': item_name,
        'item_value': item_value,
        'cancel_url': cancel_url,
    })
