import uuid
from django.db import models

from usuarios.models import User
from productos.models import Producto
from django.db.models.signals import pre_save
# Create your models here.

class Carrito(models.Model):
    cart_id = models.CharField(max_length=100,null=False,blank=False,unique=True)
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)#relacion de uno a muchos con el modelo usuario
    productos = models.ManyToManyField(Producto)#relacion muchos a muchos con el modelo productos
    subtotal = models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    total = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
def set_cart_id(sender,instance,*arg,**kwargs):#creamos un callbacks
    
     if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())#aca se genera un id aleatorio para no trabajar con el id original del carrito de compras 

pre_save.connect(set_cart_id, sender=Carrito)

