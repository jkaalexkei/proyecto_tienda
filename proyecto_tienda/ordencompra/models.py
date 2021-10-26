from enum import Enum
from django.db import models
from usuarios.models import User
from carrito.models import Carrito


# Create your models here.

class OrderStatus(Enum):
    #estados de la orden
    CREADO='CREADO'#CREATED
    PAGADO='PAGADO'#PAYED
    COMPLETADO='COMPLETADO'#COMPLETED
    CANCELADO='CANCELADO'#CANCELED


opciones = [( tag, tag.value) for tag in OrderStatus ]


class Ordencompra(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    cart = models.ForeignKey(Carrito,on_delete=models.CASCADE)

    status = models.CharField(max_length=50,choices=opciones,default=OrderStatus.CREADO)#enum

    total_envio =  models.DecimalField(default=5,max_digits=8,decimal_places=2)

    total = models.DecimalField(default=0,max_digits=8,decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''





