
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from . forms import FormularioRegistro
#from django.contrib.auth.models import User
from usuarios.models import User
from productos.models import Producto

def index(request):

    prod = Producto.objects.all().order_by('-id') #esto ordena los productos del mas nuevo al mas antiguo

    return render(request,'inicio.html',{

        'titulo':'Listado de Articulos',
        'productos':prod

         })
        
        # 'saludo': 'este es el saludo',
        # 'titulo':'Listado de Articulos',
        # 'productos':[
        #     {'titulo':'A','precio':1,'stock':True,'imagen':"{% static 'img/user.jpg' %}"},
        #     {'titulo':'B','precio':2,'stock':False},
        #     {'titulo':'C','precio':3,'stock':True},
            
        # ]
   


def iniciodesesion(request):

    if request.user.is_authenticated:#esta comprobacion valida si el usuario esta autenticado y evita que acceda a otras url sin estar autenticado
        return redirect ('index')
    
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
    
    if request.user.is_authenticated:#esta comprobacion valida si el usuario esta autenticado y evita que acceda a otras url sin estar autenticado
        return redirect ('index')

    formulario = FormularioRegistro( request.POST or None)
    #aca se pueden pasar valores por defecto en un diccionario al formulario

    if request.method == 'POST' and formulario.is_valid():
        # usuario = request.POST.get('usuario')
        # clave = request.POST.get('clave')
        # correo = request.POST.get('correo')

        # print(usuario,' ',clave,' ',correo)

        # nuevousuario = User.objects.create_user(usuario, correo, clave)
        nuevousuario = formulario.save()#los datos del formulario son capturados en el archivo forms.py
#el metodo create_user crea un objeto de tipo user pero sin permisos de admin y se encarga de encriptar la clave de manera automatica
        if nuevousuario:
            login(request,nuevousuario)
            messages.success(request,'usuario creado exitosamente')
            return redirect('index')
   
    
    
    return render(request,'usuarios/registro.html',{
        'forms':formulario
    })