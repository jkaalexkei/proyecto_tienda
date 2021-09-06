from django.shortcuts import render

# Create your views here.


def carrito(request):

    #el atributo sesion es una diccionario
    #para crear una nueva sesion se debe crear una nueva clave con su respectiv0 valor
    #la sesion se crea en el objeto request
    request.session['carrito_id'] = '123'#aca creamos una nueva sesion




    return render(request,'carrito/carrito.html',{

    })