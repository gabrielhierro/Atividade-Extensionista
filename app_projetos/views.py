from django.shortcuts import render
from .models import Projeto  # Importe o modelo Projeto

def projeto_view(request):
    projetos = Projeto.objects.all()  # Busca todos os projetos no banco de dados
    context = {'projetos': projetos}  # Cria um dicionário de contexto com a lista de projetos
    return render(request, 'projetos/projetos.html', context)