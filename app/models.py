from django.db import models

# Create your models here.

class Filme(models.Model):
    titulo = models.CharField('título', max_length=100 , unique=True)
    imagem = models.ImageField(upload_to='images')
    ano = models.CharField(max_length=10)
    duracao = models.CharField('duração', max_length=5)
    classificacao = models.CharField('classificação', max_length=100)
    genero = models.CharField('gênero',max_length=100)	
    diretor = models.CharField(max_length=100)
    sinopse = models.TextField()

    def __str__(self):
        return self.titulo