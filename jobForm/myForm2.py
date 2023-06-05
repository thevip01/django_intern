from django import forms
from .models import UserRegisterModel


class UserRegistrationForm(forms.Form):

    firstname = forms.CharField(
        label="First Name", min_length=3)
    lastname = forms.CharField(label="Last Name", min_length=3)
    username = forms.CharField(min_length=3, max_length=16)
    email = forms.EmailField(label="Email")
    phone = forms.IntegerField(label="Phone Number")
    password = forms.CharField()

    firstname.widget.attrs['class'] = 'form-control'
    lastname.widget.attrs['class'] = 'form-control'
    username.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    phone.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'
