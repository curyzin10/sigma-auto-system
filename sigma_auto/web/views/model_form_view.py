from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.http import Http404
from django.apps import apps

def model_form_view(request, model_name, pk=None):
    # Tente obter o modelo dinamicamente com base no nome
    try:
        model = apps.get_model('app_name', model_name)  # Substitua 'app_name' pelo nome do seu app
    except LookupError:
        raise Http404("Modelo não encontrado")

    # Criar o formulário dinamicamente para o modelo
    Form = modelform_factory(model, exclude=[])  # Exclua ou inclua campos conforme necessário
    instance = None

    # Se estamos editando um objeto existente
    if pk:
        instance = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = Form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')  # Substitua com a URL da lista geral ou use uma URL dinâmica
    else:
        form = Form(instance=instance)

    return render(request, 'cliente/generic_form.html', {
        'form': form,
        'model_name': model_name,
        'instance': instance,
        'pk': pk,
    })
