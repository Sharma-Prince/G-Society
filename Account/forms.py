from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ExtendedUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'padding'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Password', 'class':'padding'}))
    phone = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","phone"]


class ExtendedCommnetForm(UserCreationForm):
    pass
class ExtendedAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'padding'}))

    class Meta:
        fields = ["username","password"]
