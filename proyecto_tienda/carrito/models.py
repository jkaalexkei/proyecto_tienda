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
    productos = models.ManyToManyField(Producto, through='CartProducts')#relacion muchos a muchos con el modelo productos
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
        self.save()#guardar cambios
    
    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Carrito.FEE))
        self.save()

    def productos_related(self):
        #esta linea permite solventar el problema n + 1 query
        return self.cartproducts_set.select_related('producto')#con esta linea estaremos obteniendo la relacion de todos los elementos cartproducts y productos mediante el uso del metodo select_related el cual hace las veces de un join en sql . Permite obtener la mayor cantidad de información posible

class CartProductsManager(models.Manager): #clase para extender funciones del objeto objects

    def crear_o_actualizar_cantidad(self,carrito,producto,cantidad=1):
            objeto , created = self.get_or_create(carrito=carrito,producto=producto) #get_or_create permite obtener un objeto a partir de condiciones retorna dos parametros. el objeto si ya existe,el objeto en que caso que se haya creado, el segundo parametro es booleano
            if not created:#siempre que el objeto se cree o actualize se actualiza la cantidad
                cantidad = objeto.cantidad + cantidad

            objeto.update_cantidad(cantidad)
                

            return objeto

class CartProducts(models.Model):
    #este modelo se encarga de establecer la rrelación entre un carrito y producto

    carrito = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    #cantidad de productos que se pueden agregar al carrito
    cantidad = models.IntegerField(default=1)
    created_at= models.DateTimeField(auto_now_add=True)

    objects = CartProductsManager()

    def update_cantidad(self,cantidad=1):
        self.cantidad = cantidad
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
        post_clear --> despues que limipia la relacion
    """


    pass
pre_save.connect(set_cart_id, sender=Carrito)
m2m_changed.connect(update_totals,sender=Carrito.productos.through)#aca se debe colocar es la relacion entre el carrito y productos

