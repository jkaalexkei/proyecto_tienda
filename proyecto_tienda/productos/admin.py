from django.contrib import admin
from . models import Producto


# Register your models here.




#este codigo a continuacion se utiliza para ocultar el campo slug en el panel de administracion y generar uno de manera automatica a partir del titulo

class ProductoAdmin(admin.ModelAdmin):
    fields = ('titulo','descripcion','precio')#este atributo debe ser una tupla y se usa para seleccionar los campos que se quieren mostrar en el admin de django

    list_display = ('__str__','slug','created')#se indica los atributos que queremos se muestren en el listado de productos en el admin de django y esto debe ser una tupla
    #se debe registrar la clase para que se visualice en el admin de django

admin.site.register(Producto, ProductoAdmin)


