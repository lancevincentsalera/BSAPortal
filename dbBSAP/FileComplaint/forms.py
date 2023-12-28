from django.forms import ModelForm
from django import forms
from django.apps import apps


Resident = apps.get_model('CreateAccount', 'Resident')


class ResidentForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your lastname'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    present_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your current address'}))

    class Meta:
        model = Resident
        fields = ['username', 'password', 'first_name', 'last_name', 'birth_date', 'present_address']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, label="username")
    password = forms.CharField(widget=forms.PasswordInput, label="password")





