

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'inicio.html',{
        
        'saludo': 'este es el saludo',
        'titulo':'Listado de Articulos',
        'productos':[
            {'titulo':'A','precio':1,'stock':True},
            {'titulo':'B','precio':2,'stock':False},
            {'titulo':'C','precio':3,'stock':True},
        ]
    })

