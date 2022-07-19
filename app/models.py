from django.db import models
from django.dispatch import receiver


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

def delete(self):
    self.FieldFile.delete(save=False)
    self.delete()

@receiver(models.signals.post_delete, sender=Filme)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.imagem.delete(save=False)
