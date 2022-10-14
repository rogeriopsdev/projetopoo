from django.db import models
from PIL import Image


# Create your models here.

class Mesa(models.Model):
    nome = models.CharField(max_length=200)
    capacidade = models.CharField(max_length=200)
    status = models.CharField(max_length=30)
    foto = models.ImageField(blank=True, null=True)

    def foto_url(self):
        if self.foto and hasattr(self.foto,'url'):
            return self.foto.url
        else:
            print('sem foto')




    def save(self):
        super().save()
        im = Image.open(self.foto.path)
        novo_tamanho =(200,200)
        im.thumbnail(novo_tamanho)
        im.save(self.foto.path)


