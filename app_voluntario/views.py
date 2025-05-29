
# Create your views here.

from django.shortcuts import render, redirect
from .forms import VoluntarioForm

def voluntario(request):
    return render(request, 'voluntario/voluntario.html')

def voluntario_view(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_de_confirmacao')  # redirecione para uma página de sucesso
    else:
        form = VoluntarioForm()

    return render(request, 'voluntario/voluntario.html', {'form': form})


def seja_voluntario(request):
    return render(request, 'voluntario/seja_voluntario.html')

