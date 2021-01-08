from django.db import models

# Create your models here.
class Link(models.Model):
    chave = models.SlugField(verbose_name="Identificação rede social",max_length=100,unique=True)
    descricao = models.CharField(verbose_name="Descrição", max_length=100)
    url = models.URLField(max_length=200,null=False,blank=False)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "link"
        verbose_name_plural = "links"
        ordering = ['chave']
    def __str__(self):
        return self.chave