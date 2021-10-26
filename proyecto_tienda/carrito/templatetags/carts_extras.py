from django import template #permite registrar funciones como filters


register = template.Library()#se crea el filtro

@register.filter()
def cantidad_product_format(cantidad=1):
    return '{} {}'.format(cantidad,'productos' if cantidad > 1 else 'producto')

@register.filter()
def cantidad_agregar_format(cantidad=1):
    return '{} {}'.format(cantidad_product_format(cantidad),
            'agregados' if cantidad > 1 else 'agregado'
            )
