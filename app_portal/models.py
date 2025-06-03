from django.db import models

# Create your models here.

from django.utils import timezone

class Comunicado(models.Model):
    titulo = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='comunicados/', blank=True, null=True)

    def __str__(self):
        return self.titulo
