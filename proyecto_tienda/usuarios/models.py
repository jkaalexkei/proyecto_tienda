from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
#esta app permite trabajar con la clase user que viene con django

#proxy model es un modelo que el cual heredar funciones de otro
#pasos

#definir una clase que hereda del modelo user
#customer = cliente

#clase AbstractUser o AbstractBaseUser(las disferencias entre ellas son los atributos que se pueden heredar)
#estas dos clases nos permiten reemplazar la clase user

""" 
#AbstractUser
    id
    password
    last_login

#AbstractBaseUser
    username
    first_name
    last_name
    email
    password
    groups
    user_permissions
    is_staff
    is_active
    is_superuser
    last_login
    date_joined

"""


class User(AbstractUser):
    
    def get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

class CustomerUsuario(User): #definicion del proxy model
    class Meta:
        proxy=True #
    
    def get_Producto(self):
        return [] #retorna productos adquiridos por el cliente
                    #retorna una lista vacia
    

class Perfil(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)#relacion 1 a 1 con el modelo usuario
    biografia = models.TextField()



''' 
    from usuarios.models import CustomerUsuario

    customer = Customer.objects.get(pk=1) --> de esta manera le pasamos a la variable todos los valores y propiedades

    customer.getProducto()

 '''