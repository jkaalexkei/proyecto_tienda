from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8,decimal_places=2) # 12345678,12
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo


    #opciones de filtrado

    # Producto.objects.filter(criterio).firts()--> devuelve el primero
    # Producto.objects.filter(criterio).last()--> devuelve el ultimo
    # Producto.objects.filter(criterio).count()--> devuelve el total de elementos encontrados
    # Producto.objects.filter(criterio).exists() --> devuelve True o False en caso que exista o no el elemento