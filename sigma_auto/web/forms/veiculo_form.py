from django import forms

from ..models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        widgets = {
            'valor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'R$ 0,00'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  # Para o campo de imagem
        }

    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        self.fields['valor'].localize = True  # Ativa a formatação local para o campo
        self.fields['valor'].widget.attrs['placeholder'] = 'R$ 0,00'  # Exemplo de placeholder
        self.fields['foto'].required = False  # Se a foto não for obrigatória, podemos fazer isso
