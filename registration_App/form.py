from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms as f


class RegistrationForm(UserCreationForm):
    username = f.CharField(label='Login', help_text='')
    password1 = f.CharField(label='Password',
                            widget=f.PasswordInput())
    password2 = f.CharField(label='Confirm Password',
                            widget=f.PasswordInput(attrs={'autocomplete': 'new-password'}))
    first_name = f.CharField(label='First Name', max_length=30, required=True)
    last_name = f.CharField(label='Last Name', max_length=30, required=True)
    email = f.EmailField(label='Email',
                         widget=f.TextInput(attrs={'placeholder': 'Enter your email address'}))