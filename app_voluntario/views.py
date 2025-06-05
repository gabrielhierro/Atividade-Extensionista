from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VoluntarioForm

def voluntario_view(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Obrigado! Sua inscrição foi salva com sucesso.')
            return redirect('app_voluntario:voluntario_view')
        else:
            # Adiciona cada erro como uma mensagem do tipo toast
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = VoluntarioForm()

    return render(request, 'voluntario/voluntario.html', {'form': form})
