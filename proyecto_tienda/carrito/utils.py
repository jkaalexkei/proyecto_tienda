from .models import Carrito

def get_or_create_carrito(request):
    
    usuario = request.user if request.user.is_authenticated else None

    carrito_id = request.session.get('carrito_id')#le asignamos a la variable la sesion existente
    #el metodo get retorna None en caso que la llave no exista

    carrito = Carrito.objects.filter(cart_id=carrito_id).first()#de esta manera retornamos una lista de objetos que cumplan la condicion de lo contrario retorna None

    if carrito is None:#validamos si el carrito no existe

        carrito = Carrito.objects.create(usuario = usuario)#creamos el carrito

    if usuario and carrito.usuario is None:#si el carrito existe y si el carrito no posee un usuario entonces
        carrito.usuario = usuario#creamos la relacion asignando el carrito al usuario
        carrito.save()#se guarda la informacion


    # if carrito_id:#en caso que sea verdadero
        #  carrito = Carrito.objects.get(cart_id=carrito_id) #obtenemos el carrito de la BD
    # else:
        # carrito = Carrito.objects.create(usuario = usuario)

    request.session['carrito_id']=carrito.cart_id #actualizamos el nombre de la sesion con el id del carrito

    return carrito