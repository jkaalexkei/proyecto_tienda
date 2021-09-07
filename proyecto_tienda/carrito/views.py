from django.shortcuts import render
from .models import Carrito
# Create your views here.


def carrito(request):

    user = request.user if request.user.is_authenticated else None

    carritoid = request.session.get('carritoid')

    if carritoid:
        carrito = Carrito.objects.get(pk=carritoid)#traemos el carrito de la BD
    else:
        carrito = Carrito.objects.create(usuario=user) #EN CASO QUE NO EXISTA SE CREA UN CARRITO
    
    request.session['carritoid'] = carrito.id

    return render(request,'carrito/carrito.html',{

    })

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


    