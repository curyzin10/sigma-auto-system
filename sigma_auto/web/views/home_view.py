from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Veiculo


# Definir uma view simples para a raiz


@login_required  # Apenas usuários autenticados poderão acessar
def home(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'home.html', {'veiculos': veiculos})
