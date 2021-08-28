from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#esta app permite trabajar con la clase user que viene con django

#proxy model es un modelo que permite heredar funciones de otro
#pasos

#definir una clase que hereda del modelo user

class CustomerUsuario(User):
    class Meta:
        proxy=True #
    
    def getProducto(self):
        return [] #retorna productos adquiridos por el cliente


''' 
    from usuarios.models import CustomerUsuario

    customer = Customer.objects.get(pk=1) --> de esta manera le pasamos a la variable todos los valores y propiedades

    customer.getProducto()

 '''