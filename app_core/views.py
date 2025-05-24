from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def sobre(request):
    return render(request, 'sobre/sobre.html')

def voluntario(request):
    return render(request, 'voluntario/voluntario.html')

def projeto(request):
    return render(request, 'projetos/projetos.html')