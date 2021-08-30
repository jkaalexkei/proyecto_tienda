from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Perfil


admin.site.register(User,UserAdmin)
admin.site.register(Perfil)

# Register your models here.

"""
    nota:
        para que las funcionalidades de autenticacion sigan funcionando 
        (login,logout,request.user,decoradores de autenticacion, otros) se debe
        modificar la constante AUTH_USER_MODEL en el archivo settings
"""