from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VoluntarioForm

def voluntario_view(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Obrigado! Sua inscrição foi salva com sucesso.')
            return redirect('app_voluntario:voluntario_view')  # redireciona para a mesma página para "limpar" o form
    else:
        form = VoluntarioForm()

    return render(request, 'voluntario/voluntario.html', {'form': form})
