from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8,decimal_places=2) # 12345678,12
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False,blank=False,unique=True)#se usa para obtener elementos a partir de su slug
    #unique--> permite almacenar valores unicos

    def __str__(self):
        return self.titulo

    #para un slug automatatico se debe sobrescribir el metodo save() de la clase padre
    # def save(self,*args,**kwargs):
    #     #generamos el slug a partir del titulo del producto
    #     self.slug = slugify(self.titulo)

    #     super(Producto,self).save(*args,**kwargs)#se hace elllamado al metodo save de la clase padre y se le ppasan los argumenos *args,**kwargs


    #esta funcion callbascks de a continuacion funciona de la misma manera que lo anterior del  metodo save
    #mediante el uso del signals pre-save

def set_slug(sender, instance,*args,**kwargs):#callbacks y recibe 5 parametros (sender, instance, raw, using, update_fields )
     instance.slug = slugify(instance.titulo)

pre_save.connect(set_slug, sender=Producto)   




    #opciones de filtrado

    # Producto.objects.filter(criterio).firts()--> devuelve el primero
    # Producto.objects.filter(criterio).last()--> devuelve el ultimo
    # Producto.objects.filter(criterio).count()--> devuelve el total de elementos encontrados
    # Producto.objects.filter(criterio).exists() --> devuelve True o False en caso que exista o no el elemento



    
#los callbacks permite ejecutar acciones antes o despues que se suscite cierto evento
#se pueden implementar los callbacks mediante el uso de signals 
#con los signals podemos implementar callbacks antes o despues que un objeto se inicialice, actualice, elimine
#se pueden ejecutar callbacks cuando ocurran cambios en una relacion de muchos a muchos
#ejemplo pre-save