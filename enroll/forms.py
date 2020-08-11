from django import forms

from .models import user

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

from django.core import validators



class studentRegister(forms.ModelForm):
    password = forms.CharField(max_length=32,  widget=forms.PasswordInput(render_value=True , attrs={'class':'form-control'})) 
    class Meta:
        model = user
        fields = ['name' , 'email' , 'password']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class SignupForm(UserCreationForm):
    password2  = forms.CharField(label = 'Conform Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
        

