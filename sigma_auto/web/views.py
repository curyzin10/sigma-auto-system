from django.shortcuts import render


def home(request):
    return render(request, 'home.html')  # Renderiza o template "home.html"


def about(request):
    return render(request, 'about.html')  # Renderiza o template "about.html"
