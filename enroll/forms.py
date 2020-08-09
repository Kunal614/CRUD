from django import forms

from .models import User

from django.core import validators


class studentRegister(forms.ModelForm):
    password = forms.CharField(max_length=32,  widget=forms.PasswordInput(render_value=True , attrs={'class':'form-control'})) 
    class Meta:
        model = User
        fields = ['name' , 'email' , 'password']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            
        }

