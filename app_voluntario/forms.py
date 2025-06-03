from django import forms
from .models import Voluntario

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome_completo', 'email', 'telefone', 'profissao']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seuemail@exemplo.com.br'}),
            'telefone': forms.TextInput(attrs={
                'type': 'tel',
                'placeholder': '(DD) 9XXXX-XXXX',
                'data-mask': '(00) 00000-0000'
            }),
            'profissao': forms.TextInput(attrs={'placeholder': 'Sua área de atuação'}),
        }