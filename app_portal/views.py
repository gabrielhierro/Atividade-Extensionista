from django.shortcuts import render

def comunicado(request):
    return render(request, 'portal/comunicados.html')