from django import forms

from django.forms.widgets import EmailInput, PasswordInput, TextInput

#clase que permite crear formularios
class FormularioRegistro(forms.Form):
    
    usuario = forms.CharField(required=True,min_length=4,max_length=20,widget=TextInput(attrs={
        'class':'form-control',
    }))
    
    clave =  forms.CharField(required=True,max_length=10,widget=EmailInput(attrs={
        'class':'form-control'
    }))
    
    correo =  forms.EmailField(required=True,max_length=50,widget=PasswordInput(attrs={
        'class':'form-control'
    }))  
    
    
