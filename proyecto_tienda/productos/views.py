
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView #modulo para trabajar en detalle con un objeto
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


#clase para visualizar un producto o articulo en detalle
#obtiene un objeto mediante su id o llave primaria
class ProductoDetailView(DetailView):
    
    model = Producto #modelo con el que se va trabajar
    template_name = 'producto/producto.html' #template con el que se va a trabajar

    #este metodo se usa para visualizar elementos en un template
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs) #esto genera un nuevo diccionario para generar nuevas llaves
        context['titulo'] = 'Listado de Productos' #aca se reemplaza lo que tiene el nombre titulo por un nuevo valor

        print(context)
        return context