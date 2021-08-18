"""proyecto_tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from . import views

from productos.views import ProductosListView #importamos la nueva clase que posee la vista de productos
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index,name='index'),aca se reemplaza esta url y se asigna la url a la clase declarada en la vista de productos por esta que sigue a continuacion
    #el metodo as_view le indica a django que dicha clase sera usada como una vista
    path('', ProductosListView.as_view() ,name='index'),
    #producto/id
    path('producto/',include('productos.urls')),#con esto le estamos indicando que podemos hacer uso de todas las rutas mediante el prefijo producto



    path('usuarios/login/',views.iniciodesesion,name='login'),
    path('usuarios/logout/',views.cerrarsesion,name='logout'),
    path('usuarios/registro/',views.registro,name='registro'),
]
