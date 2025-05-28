from django.contrib import admin

from .models import Comunicado

# Register your models here.



@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    ordering = ('-data_publicacao',)
    search_fields = ('titulo', 'mensagem')
