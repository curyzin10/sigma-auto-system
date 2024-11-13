from django import forms

from ..models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        widgets = {
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        self.fields['valor'].localize = True  # Ativa a formatação local para o campo
        self.fields['valor'].widget.attrs['placeholder'] = 'R$ 0,00'  # Exemplo de placeholder
