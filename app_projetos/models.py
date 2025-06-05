from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos_imagens/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo


    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'