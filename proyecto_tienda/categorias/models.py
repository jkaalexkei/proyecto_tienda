from django.db import models
from productos.models import Producto
# Create your models here.


class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #relacion a muchos a muchos

    producto = models.ManyToManyField(Producto)

    def  __str__(self):
        return self.titulo
        

