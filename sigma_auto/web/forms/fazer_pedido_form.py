from django import forms

from ..models import Pedido


class FazerPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
