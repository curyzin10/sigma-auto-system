from django import forms
from ..models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
