from django import forms
from django.contrib.auth.hashers import check_password, make_password

from .models import Bkuser



class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required': 'Enter Email'},
        max_length=64, label='Email'
    )
    password = forms.CharField(
        error_messages={'required': 'Enter Password'},
        widget=forms.PasswordInput, label='Password'
    )
    re_password = forms.CharField(
        error_messages={'required': 'Enter Password'},
        widget=forms.PasswordInput, label='Re_Password'
    )

    def clean(self):
        # Check password if identical
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', 'Passwords are not identical')
                self.add_error('re_password', 'Passwords are not identical')



class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required': 'Enter Email'},
        max_length=64, label='Email'
    )
    password = forms.CharField(
        error_messages={'required': 'Enter Password'},
        widget=forms.PasswordInput, label='Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                bkuser = Bkuser.objects.get(email=email)
            except Bkuser.DoesNotExist:
                self.add_error('smail', 'No Email found.')
                return

            if not check_password(password, bkuser.password):
                self.add_error('password', 'Password is wrong.')
            else:
                self.email = bkuser.email