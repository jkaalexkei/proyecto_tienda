
from django.urls.conf import path

from . import views

app_name = 'productos'

urlpatterns = [
    #esta url recibe la llave primaria como parametro para la consulta del objeto
    path('buscar',views.ProductoBuscadorListView.as_view(),name='buscar'),#url del buscador
    path('<slug:slug>',views.ProductoDetailView.as_view(),name='producto'),
    
]