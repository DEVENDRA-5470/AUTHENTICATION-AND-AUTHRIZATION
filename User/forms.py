
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django import forms


class Signup_form(UserCreationForm):
    password1=forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={"placeholder":"Password"}),
    )
    password2=forms.CharField(label="Confirm Password", 
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
    

        error_messages = {
        'username': {
            'unique': _('The username is not available')
        },
        'first_name': {
            'required': _('The field can not be empty')
        },
        'last_name': {
            'required': _('The field can not be empty')
        },
      

    }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for field_name in self.fields:
            field = self.fields[field_name]
            field.required = True
    


class Login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Username", 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'placeholder': "Password", 'class': 'form-control'}))


   

  

