from django.shortcuts import render, redirect
from ..forms.contato_form import ContatoForm


def contato_view(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco
            return redirect('contato_enviado')  # Redireciona para uma página de sucesso
    else:
        form = ContatoForm()

    return render(request, 'home.html', {'form': form})


def contato_enviado_view(request):
    return render(request, 'contato_enviado.html')
