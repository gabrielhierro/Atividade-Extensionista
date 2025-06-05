from django.contrib import admin
from .models import Voluntario

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email','cpf', 'telefone', 'profissao', 'data_inscricao')
