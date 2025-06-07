from django.db import models

class Voluntario(models.Model):
    nome_completo = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    profissao = models.CharField(max_length=100)
    data_inscricao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = 'Voluntário'      
        verbose_name_plural = 'Voluntários'  