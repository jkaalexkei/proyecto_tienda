import uuid
from django.db import models

from usuarios.models import User
from productos.models import Producto
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed #signals para calcular subtotal y total del carrito de compras
import decimal

# Create your models here.

class Carrito(models.Model):
    cart_id = models.CharField(max_length=100,null=False,blank=False,unique=True)
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)#relacion de uno a muchos con el modelo usuario
    productos = models.ManyToManyField(Producto)#relacion muchos a muchos con el modelo productos
    subtotal = models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    total = models.DecimalField(default=0.0,max_digits=8,decimal_places=2)
    created_ad = models.DateTimeField(auto_now_add=True)

    FEE = 0.05  #comision 5%

    def __str__(self):
        return self.cart_id
    
    def update_totals(self):
        self.update_subtotal()
        self.update_total()
    
    def update_subtotal(self):
        self.subtotal = sum([ producto.precio for producto in self.productos.all() ])#obtenemos la lista de precios y sumamos los valores
        self.save()
    
    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Carrito.FEE))
        self.save()


def set_cart_id(sender,instance,*arg,**kwargs):#creamos un callbacks
    
     if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())#aca se genera un id aleatorio para no trabajar con el id original del carrito de compras 


def update_totals(sender,instance,action,*args,**kwargs):

    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':

        instance.update_totals()

    """
        acciones que se pueden realizar para calcular el subtotal
        post_add --> despues que el objeto se agrega
        post_remove --> despues que un objeto se elimina
        post_clear --> despues que elimina la relacion
    """


    pass
pre_save.connect(set_cart_id, sender=Carrito)
m2m_changed.connect(update_totals,sender=Carrito.productos.through)

