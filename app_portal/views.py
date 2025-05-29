from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

def comunicado(request):
    comunicados = Comunicado.objects.order_by('-data_publicacao')
    return render(request, 'portal/comunicados.html', {'comunicados': comunicados})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Comunicado
from .forms import ComunicadoForm

def lista_comunicados(request):
    comunicados = Comunicado.objects.order_by('-data_publicacao')
    return render(request, 'comunicados/lista.html', {'comunicados': comunicados})

@staff_member_required
def novo_comunicado(request):
    if request.method == 'POST':
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_comunicados')
    else:
        form = ComunicadoForm()
    return render(request, 'comunicados/form.html', {'form': form, 'titulo': 'Novo Comunicado'})

@staff_member_required
def editar_comunicado(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    if request.method == 'POST':
        form = ComunicadoForm(request.POST, instance=comunicado)
        if form.is_valid():
            form.save()
            return redirect('lista_comunicados')
    else:
        form = ComunicadoForm(instance=comunicado)
    return render(request, 'comunicados/form.html', {'form': form, 'titulo': 'Editar Comunicado'})

@staff_member_required
def deletar_comunicado(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    if request.method == 'POST':
        comunicado.delete()
        return redirect('lista_comunicados')
    return render(request, 'comunicados/confirmar_exclusao.html', {'comunicado': comunicado})
