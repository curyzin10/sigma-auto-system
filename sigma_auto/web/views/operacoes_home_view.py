from django.shortcuts import render, get_object_or_404, redirect


def operacoes_page(request):
    return render(request, 'operacoes/operacoes.html', )


def operacao_venda_page(request):
    return render(request, 'operacoes/operacao_venda.html', )


def operacao_compra_page(request):
    return render(request, 'operacoes/operacao_compra.html', )


def fazer_pedido_page(request):
    return render(request, 'operacoes/fazer_pedido.html', )
