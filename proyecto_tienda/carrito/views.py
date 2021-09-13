from django.shortcuts import render
from .models import Carrito
from .utils import get_or_create_carrito
from productos.models import Producto
# Create your views here.

def carrito(request):
    carrito = get_or_create_carrito(request)
    
    return render(request,'carrito/carrito.html',{

    })
    #crear sesion
    #la sesion se crea en el objeto request
    # request.session['carrito_id'] = '123'

    #consultar sesion
    #obtenemos el valor de una sesion
    #valorsesion = request.session.get('carrito_id')

    #eliminar una sesion
    # valorsesion=request.session['carrito_id'] = None
    # print(valorsesion)

def agregar(request):
    carrito = get_or_create_carrito(request)
    prod = Producto.objects.get(pk=request.POST.get('producto_id'))
    carrito.productos.add(prod)

    return render(request,'carrito/agregar.html',{
        'producto' : prod
    })
    
   


# def sesioncarrito(request):
#     request.session['carrito_id'] = '123'
    
#     return render(request,'carrito/carrito.html',{

#     })

    # #si el usuario esta autenticado nos devuelve el usuario actual de lo contrario devuelve none
    # user = request.usuario if request.usuario.is_authenticated else None

    # carritoid = request.session.get('carrito_id')

    # if carritoid:
    #     carrito = Carrito.objects.get(pk=carritoid)#traemos el carrito de la BD mediante la variable carritoid
    # else:
    #     carrito = Carrito.objects.create(usuario=user) #EN CASO QUE NO EXISTA SE CREA UN CARRITO en funcion de si el usuario esta autenticado o no
    
    # request.session['carrito_id'] = carrito.id#la sesion almacena el id del carrito

    

    #el atributo sesion es un diccionario
    #para crear una nueva sesion se debe crear una nueva clave con su respectiv0 valor
    #la sesion se crea en el objeto request

    #crear una sesion
    #request.session['carrito_id'] = '123'#aca creamos una nueva sesion
                   #nombre de la sesion = valor de la sesion
    
    #consultar una sesion
    # valorsesion = request.session.get('carrito_id')
    # print(valorsesion)

    # #Eliminar un sesion
    # request.session['carrito_id'] = None #para eliminar se le asigna a la sesion el valor de None
    # print(valorsesion)

    #comprobacion de carrito de comprar utilizando las sesiones
    # user = request.user if request.user.is_authenticated else None

    # carrito_id = request.session.get('carrito_id')

    # if carrito_id:
    #     #obtenemos el carrito de la base de datos
    #     carrito = Carrito.objects.get(pk=carrito_id)
        
    # else:#se crea un nuevo carrito
    #     carrito = Carrito.objects.create(usuario = user)
        
    # request.session['carrito_id'] = carrito.id


    