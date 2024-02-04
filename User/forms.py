from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Signup_form(UserCreationForm):
    password1=forms.CharField(label="Password", max_length=10 ,min_length=4,
    widget=forms.PasswordInput(attrs={"placeholder":"Password"})
    )
    password2=forms.CharField(label="Confirm Password", max_length=10 ,min_length=4,
    widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"})
    )
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
    
        widgets={
        'username':forms.TextInput(attrs={'placeholder':"Username"}),
        'email':forms.EmailInput(attrs={'placeholder':"Email Address"}),
        'first_name':forms.TextInput(attrs={'placeholder':"First Name"}),
        'last_name':forms.TextInput(attrs={'placeholder':"Last Name"}),
        }
    


