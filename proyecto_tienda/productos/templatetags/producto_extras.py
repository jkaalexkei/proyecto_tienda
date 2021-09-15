from django import template

register =template.Library()#se genera una instancia del objeto Library



#generamos una nueva instancia ya se pueden registrar las funciones como filter
#los filter deben ser funciones que hagan tareas sencillas
@register.filter()
def precio_formato(valor):

    return '${0:.2f}'.format(valor)