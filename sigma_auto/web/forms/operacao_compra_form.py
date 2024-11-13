from django import forms

from ..models import OperacaoDeCompra


class OperacaoDeCompraForm(forms.ModelForm):
    class Meta:
        model = OperacaoDeCompra
        fields = '__all__'

