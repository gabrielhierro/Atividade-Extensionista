from django.shortcuts import render
from .models import Projeto

def projeto_view(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'projetos/projetos.html', context)