from django import forms

from .models import user

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , PasswordChangeForm , UserChangeForm

from django.core import validators



class studentRegister(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name' , 'email' , 'Class' , 'Comments']
        labels={'Comments':'Remarks'}
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'Class':forms.TextInput(attrs={'class':'form-control'}),
            'Comments':forms.TextInput(attrs={'class':'form-control'}),
            
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
    
class Changepass(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"})) 
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':"form-control"})) 
    new_password2 = forms.CharField(label='Conform Password' , widget=forms.PasswordInput(attrs={'class':"form-control"})) 
        
class UserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name','email' ,'date_joined' , 'last_login']
        labels = {'email':'Email','username':'Username'}
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'date_joined':forms.TextInput(attrs={'class':'form-control'}),
            'last_login':forms.TextInput(attrs={'class':'form-control'}),
        }
