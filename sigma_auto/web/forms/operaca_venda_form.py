from django import forms

from ..models import OperacaoDeVenda


class OperacaoDeVendaForm(forms.ModelForm):
    class Meta:
        model = OperacaoDeVenda
        fields = '__all__'
