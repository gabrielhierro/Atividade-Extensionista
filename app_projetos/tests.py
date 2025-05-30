from django.shortcuts import render
from .models import Projeto

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})
