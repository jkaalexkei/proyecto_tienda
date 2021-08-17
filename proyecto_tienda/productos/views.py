
from django.shortcuts import render
from django.views.generic.list import ListView
from productos.models import Producto

# Create your views here.


class ProductosListView(ListView):

    #se deben pasar dos parametro para listar objetos
    template_name = 'inicio.html' #nombre del template que se va a utilizar
    
    #consulta que permite obtener el listado de objetos
    queryset = Producto.objects.all().order_by('-id') #ordena del mas nuevo al mas reciente

    #para que la informacion se pinte en el template se debe sobreescribir el metodo
    # get_context_data() para obtener el contexto de la clase padre

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs) #esto genera un nuevo diccionario para generar nuevas llaves
        context['titulo'] = 'Listado de Productos' #aca se reemplaza lo que tiene el nombre titulo por un nuevo valor

        print(context)
        return context
