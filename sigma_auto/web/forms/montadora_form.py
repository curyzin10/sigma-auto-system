from django import forms

from ..models import Montadora


class MontadoraForm(forms.ModelForm):
    class Meta:
        model = Montadora
        fields = '__all__'
