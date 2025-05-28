from django import forms
from .models import Comunicado

class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ['titulo', 'mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 5})
        }
