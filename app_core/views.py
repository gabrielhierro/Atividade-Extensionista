from django.shortcuts import render
from app_portal.models import Comunicado

def home(request):
    ultimo_comunicado = Comunicado.objects.order_by('-data_publicacao').first()
    return render(request, 'home/index.html', {'ultimo_comunicado': ultimo_comunicado})

def sobre(request):
    return render(request, 'sobre/sobre.html')

def not_found(request, exception):
    return render(request, 'templates/not_found/404.html', status=404)