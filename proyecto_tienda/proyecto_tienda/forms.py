from django import forms
#from django.contrib.auth.models import User
from usuarios.models import User
from django.forms.widgets import EmailInput, PasswordInput, TextInput

#clase que permite crear formularios
class FormularioRegistro(forms.Form):
    
    usuario = forms.CharField(required=True,min_length=4,max_length=20,widget=TextInput(attrs={
        'class':'form-control',
    }))
    
    clave =  forms.CharField(required=True,max_length=10,widget=PasswordInput(attrs={
        'class':'form-control'
    }))

    clave2 = forms.CharField(label='Confirme la clave',required=True,max_length=10,widget=PasswordInput(attrs={
        'class':'form-control'
    }))
    
    correo =  forms.EmailField(required=True,max_length=50,widget=EmailInput(attrs={
        'class':'form-control'
    })) 

    def clean_usuario(self):#hace referencia al nombre del campo declarado en la clase formularioregistro
        #la palabra clean le indica a django que se va a realizar una validacion sobre ese campo
        #el metodo hace referencia al input del formulario que se va a validar

        username = self.cleaned_data.get('usuario')#aca se obtiene la informacion del input

        if User.objects.filter(username=username).exists():

            raise forms.ValidationError('el usuario ya existe')

        return username
    
    def clean_correo(self):

        correo = self.cleaned_data.get('correo')

        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError('el correo ya esta en uso')
        
        return correo
    
    #para validar que las contraseñas coincidan se debe sobreescribir el metodo clean de la siguiente manera. Posteriormente se hace el llamado mediante el uso de la clase super al metodo clean de la clase padre en este caso la clase Form

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('clave2') != cleaned_data.get('clave'):
            self.add_error('clave2','la clave no coincide')
            
    def save(self):
        #aca se capturan los datos y se crea el nuevo usuario
        nuevousuario=User.objects.create_user(
            self.cleaned_data.get('usuario'),
            self.cleaned_data.get('correo'),
            self.cleaned_data.get('clave'),
        )
    
        return nuevousuario