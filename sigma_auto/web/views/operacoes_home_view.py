from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required  # Apenas usuários autenticados poderão acessar
def operacoes_page(request):
    return render(request, 'operacoes/operacoes.html', )


@login_required  # Apenas usuários autenticados poderão acessar
@login_required  # Apenas usuários autenticados poderão acessar@login_required  # Apenas usuários autenticados poderão acessar
def operacao_venda_page(request):
    return render(request, 'operacoes/operacao_venda.html', )


@login_required  # Apenas usuários autenticados poderão acessar
def operacao_compra_page(request):
    return render(request, 'operacoes/operacao_compra.html', )


@login_required  # Apenas usuários autenticados poderão acessar
def fazer_pedido_page(request):
    return render(request, 'operacoes/fazer_pedido.html', )
