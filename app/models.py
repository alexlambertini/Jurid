from django.db import models

# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(max_length=100 , unique=True)
    ano = models.TextField()
    classificacao = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)	
    diretor = models.CharField(max_length=100)
    sinopse = models.TextField()
    imagem = models.ImageField(upload_to='static/imagens')

    def __str__(self):
        return self.titulo