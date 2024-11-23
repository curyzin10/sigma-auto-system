from django.urls import path
from .views import model_form_view, client_view, veiculo_view, montadora_view, vendedor_view, home_view, \
    operacoes_home_view, operacao_compra_view, operacao_venda_view, fazer_pedido_view, custom_login_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view.home, name='home'),
    path('login/', custom_login_view.CustomLoginView.as_view(), name='login'),
    path('clientes/', client_view.cliente_list, name='cliente_list'),
    path('clientes/criar/', client_view.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', client_view.cliente_update, name='cliente_update'),
    path('clientes/deletar/<int:pk>/', client_view.cliente_delete, name='cliente_delete'),
    path('veiculos/', veiculo_view.veiculo_list, name='veiculo_page'),
    path('veiculos/detalhes/<int:pk>/', veiculo_view.veiculo_detalhes, name='veiculo_detalhes'),
    path('veiculos/criar/', veiculo_view.veiculo_create, name='veiculo_create'),
    path('veiculos/editar/<int:pk>/', veiculo_view.veiculo_update, name='veiculo_update'),
    path('veiculos/deletar/<int:pk>/', veiculo_view.veiculo_delete, name='veiculo_delete'),
    path('montadoras/', montadora_view.montadora_list, name='montadora_list'),
    path('montadoras/criar/', montadora_view.montadora_create, name='montadora_create'),
    path('montadoras/editar/<int:pk>/', montadora_view.montadora_update, name='montadora_update'),
    path('montadoras/deletar/<int:pk>/', montadora_view.montadora_delete, name='montadora_delete'),
    path('vendedores/', vendedor_view.vendedor_list, name='vendedor_list'),
    path('vendedores/criar/', vendedor_view.vendedor_create, name='vendedor_create'),
    path('vendedores/editar/<int:pk>/', vendedor_view.vendedor_update, name='vendedor_update'),
    path('vendedores/deletar/<int:pk>/', vendedor_view.vendedor_delete, name='vendedor_delete'),

    path('operacoes/', operacoes_home_view.operacoes_page, name='operacoes_page'),

    path('operacoes/compra', operacao_compra_view.operacao_compra_list, name='operacao_compra'),
    path('operacoes/compra/criar/', operacao_compra_view.operacao_compra_create,
         name='operacao_compra_create'),
    path('operacoes/compra/editar/<int:pk>/', operacao_compra_view.operacao_compra_update,
         name='operacao_compra_update'),
    path('operacoes/compra/deletar/<int:pk>/', operacao_compra_view.operacao_compra_delete,
         name='operacao_compra_delete'),

    path('operacoes/venda', operacao_venda_view.operacao_venda_list, name='operacao_venda'),
    path('operacoes/venda/criar/', operacao_venda_view.operacao_venda_create,
         name='operacao_venda_create'),
    path('operacoes/venda/editar/<int:pk>/', operacao_venda_view.operacao_venda_update,
         name='operacao_venda_update'),
    path('operacoes/venda/deletar/<int:pk>/', operacao_venda_view.operacao_venda_delete,
         name='operacao_venda_delete'),

    path('operacoes/pedido', fazer_pedido_view.fazer_pedido_list, name='fazer_pedido'),
    path('operacoes/pedido/criar/', fazer_pedido_view.fazer_pedido_create, name='fazer_pedido_create'),
    path('operacoes/pedido/editar/<int:pk>/', fazer_pedido_view.fazer_pedido_update,
         name='fazer_pedido_update'),
    path('operacoes/pedido/deletar/<int:pk>/', fazer_pedido_view.fazer_pedido_delete,
         name='fazer_pedido_delete'),

    path('formulario/<str:model_name>/', model_form_view.model_form_view, name='model_form'),
    path('formulario/<str:model_name>/<int:pk>/', model_form_view.model_form_view,
         name='model_form_edit'),
]

# Servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
