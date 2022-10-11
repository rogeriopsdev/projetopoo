from django.db import models
import PIL


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
