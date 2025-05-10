from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.password_validation import validate_password


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='', 
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-group',
            'placeholder':'username'
        }))
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class':'form-group',
            'placeholder':'password',
            'type':'password'
        }))
    
    
    
class SignupForm(forms.Form):
    username = forms.CharField(
        label='', 
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-group',
            'placeholder':'username'
        }))
    email = forms.EmailField(
        label='', 
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-group',
            'placeholder':'email'
        }))
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class':'form-group',
            'placeholder':'password',
            'type':'password'
        }))
    
    password_confirm= forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class':'form-group',
            'placeholder':'confirm password',
            'type':'password'
        }))
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("This Username Already Exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This Email Already Exists")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        password_confirm = cleaned_data["password_confirm"]

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords Does Not Match")
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password
        
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user
    



        
    


                

        
    