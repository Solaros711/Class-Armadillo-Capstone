from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.core.exceptions import ValidationError

class CustomUserForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=5, max_length=26)
    email = forms.EmailField(label='Enter Email')
    password_enter = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def check_username(self):
        username = self.cleaned_data['username'].lower()
        check = User.objects.filter(username=username)
        if check.count():
            raise ValidationError('This Username already exists.')

    def check_email(self):
        email = self.cleaned_data['email'].lower()
        check = User.objects.filter(email=email)
        if check.count():
            raise ValidationError('This Email already exists.')

    def check_password(self):
        password_enter = self.cleaned_data['password_enter'].lower()
        password_confirm = self.cleaned_data['password_confirm'].lower()
        
        if password_enter != password_confirm:
            raise ValidationError('The Password does not match.')
        return password_confirm

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password_confirm']
        )