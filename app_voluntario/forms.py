from django import forms
from .models import Voluntario
from validate_docbr import CPF

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome_completo', 'email', 'cpf', 'telefone', 'profissao']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seuemail@exemplo.com.br'}),
            'cpf': forms.TextInput(attrs={
                'placeholder': 'XXX.XXX.XXX-XX',
                'data-mask': '000.000.000-00'
            }),
            'telefone': forms.TextInput(attrs={
                'type': 'tel',
                'placeholder': '(DD) 9XXXX-XXXX',
                'data-mask': '(00) 00000-0000'
            }),
            'profissao': forms.TextInput(attrs={'placeholder': 'Sua área de atuação'}),
            
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf_validator = CPF()

        if not cpf_validator.validate(cpf):
            raise forms.ValidationError("CPF inválido.")
        
        if Voluntario.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado como voluntário.")
        
        return cpf