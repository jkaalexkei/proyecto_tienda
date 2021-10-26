from django.shortcuts import redirect, render
#from .models import Carrito
from .models import Producto
from .utils import get_or_create_carrito
from django.shortcuts import get_object_or_404 #para manejar excepciones en los templates
from .models import CartProducts

# Create your views here.

def carrito(request):

    cart = get_or_create_carrito(request)
    
    return render(request, 'carrito/carrito.html',{
        'cart':cart
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

def agregar(request):#vista para agregar elementos al carrito
    carrito = get_or_create_carrito(request)#obtenemos el carrito
    prod = Producto.objects.get(pk=request.POST.get('producto_id'))#obtenemos el producto
    cantidad = int(request.POST.get('cantidad',1)) #aca capturamos el valor del formulario para la cantidad, que caso que no se suministre ningun valor toma el valor por defecto 1

    #otra manera para agregar elementos al carrito y crear la relacion con el modelo producto es siguiente
    
    # cart_producto=CartProducts.objects.created_or_update_cantidad(carrito=carrito,producto=prod,cantidad=cantidad)
    cart_producto=CartProducts.objects.crear_o_actualizar_cantidad(carrito=carrito,producto=prod,cantidad=cantidad)


    # carrito.productos.add(prod, through_defaults={
    #     'cantidad':cantidad

    # })#agregamos la relacion
    #el parametro through_default es un diccionario y se utiliza para establecer valores a los atributos de la vista

    return render(request,'carrito/agregar.html',{
        'cantidad':cantidad,
        'cart_product': cart_producto,
        'producto' : prod#enviamos el producto al template

    })

def remove(request):
    carrito = get_or_create_carrito(request)#obtenemos el carrito

    prod = get_object_or_404(Producto,pk=request.POST.get('producto_id'))
        #sintaxis  get_object_or_404(Modelo a trabajar,condicion a evaluar)
    #prod = Producto.objects.get(pk=request.POST.get('producto_id'))#obtenemos el producto que queremos eliminar

    """
    La diferencia entre la excepcion y la pagina 404 es que la excepcion manda un con codigo 500 al cliente indicando que hubo un error interno en el servidor.

    la page not found envia un codigo 404 indicando al cliente que un recurso no pudo ser encontrado
    """

    carrito.productos.remove(prod)

    return redirect('carrito:carrito')
   


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


    