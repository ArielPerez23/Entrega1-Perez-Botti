from django import forms
from django.forms import ModelForm

from authorization.forms import *

from .models import Article

# choices = [('Curiosidades','Curiosity'),('Software','Software'),('Hardware','Hardware')]

# class NewArticle(forms.Form):
    
#     title = forms.CharField(label='Titulo', max_length=150)
#     subtitle = forms.CharField(label='Subtitulo', max_length=200, required=False)
#     body = forms.CharField(label='Contenido', widget=forms.Textarea)
#     image = forms.ImageField(label='Imagen', required=False)
#     category = forms.ChoiceField(label='Categoria', choices=choices)

class NewArticle(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    pasword2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    class Meta:
    
        model = User
        fields = ('__all__')
    
        help_texts = {k:"" for k in fields}