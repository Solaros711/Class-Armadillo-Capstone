from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.core.exceptions import ValidationError

class CustomUserForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=5, max_length=26)
    email = forms.EmailField(label='Enter Email')
    password_enter = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cd = self.cleaned_data
        
        check_username = User.objects.filter(username=cd.get('username'))
        if check_username.count() > 0:
            self.add_error('email', 'This username already exists!')

        check_email = User.objects.filter(email=cd.get('email'))
        if check_email.count() > 0:
            self.add_error('email', 'This email already exists!')

        if cd.get('password_enter') != cd.get('password_confirm'):
            self.add_error('password_confirm', 'passwords do not match!')
        return cd
        

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password_confirm']
        )