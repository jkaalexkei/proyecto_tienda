from django.db import models
from django.db.models.deletion import CASCADE
from usuarios.models import User
from productos.models import Producto
# Create your models here.

class Carrito(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)#relacion de uno a muchos con el modelo usuario
    productos = models.ManyToManyField(Producto)#relacion muchos a muchos con el modelo productos
    subtotal = models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    total = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''
