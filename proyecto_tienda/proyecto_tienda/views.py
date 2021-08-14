
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from . forms import FormularioRegistro


def index(request):
    return render(request,'inicio.html',{
        
        'saludo': 'este es el saludo',
        'titulo':'Listado de Articulos',
        'productos':[
            {'titulo':'A','precio':1,'stock':True,'imagen':"{% static 'img/user.jpg' %}"},
            {'titulo':'B','precio':2,'stock':False},
            {'titulo':'C','precio':3,'stock':True},
            
        ]
    })


def iniciodesesion(request):
    
    if request.method == 'POST':
        
        usuario = request.POST.get('username')
        clave = request.POST.get('password')
        
        persona = authenticate(username=usuario,password=clave)
       
        if persona:
           login(request,persona)
           messages.success(request,'Sesión Iniciada Correctamente {}'.format(usuario))
           return redirect('index')
        else:
            messages.error(request,'Sesión no Iniciada')         
        
    
    return render(request,'usuarios/login.html',{
        
      
        
    })

def cerrarsesion(request):
    
    logout(request)
    messages.success(request,'Sesión cerrada exitosamente')
    return redirect ('login')


def registro(request):
    
   
    formulario = FormularioRegistro()
    
    
    
    return render(request,'usuarios/registro.html',{
        'forms':formulario
    })