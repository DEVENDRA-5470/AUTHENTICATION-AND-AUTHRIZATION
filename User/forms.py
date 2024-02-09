
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from django import forms


class Signup_form(UserCreationForm):
    password1=forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={"placeholder":"Password", 'class': 'form-control shadow-none'}),
    )
    password2=forms.CharField(label="Confirm Password", 
    widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password", 'class': 'form-control shadow-none'})
    )
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

    
        widgets={
        'username':forms.TextInput(attrs={'placeholder':"Username", 'class': 'form-control shadow-none'}),
        'email':forms.EmailInput(attrs={'placeholder':"Email Address", 'class': 'form-control shadow-none'}),
        'first_name':forms.TextInput(attrs={'placeholder':"First Name", 'class': 'form-control shadow-none'}),
        'last_name':forms.TextInput(attrs={'placeholder':"Last Name", 'class': 'form-control shadow-none'}),
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
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': "Username", 'class': 'form-control shadow-none'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'placeholder': "Password", 'class': 'form-control shadow-none'}))

class ch_pass_form(PasswordChangeForm):
    class Meta:
        model = User 
        fields = ['old_password', 'new_password1', 'new_password2']






   


   

  

