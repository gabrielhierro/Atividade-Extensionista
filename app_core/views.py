from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def sobre(request):
    return render(request, 'sobre/sobre.html')

def voluntario(request):
    return render(request, 'voluntario/voluntario.html')

def projeto(request):
    return render(request, 'projetos/projetos.html')

from app_portal.models import Comunicado

def home(request):
    ultimo_comunicado = Comunicado.objects.order_by('-data_publicacao').first()
    return render(request, 'home/index.html', {'ultimo_comunicado': ultimo_comunicado})