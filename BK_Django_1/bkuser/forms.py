from django import forms
from django.contrib.auth.hashers import check_password
from .models import Bkuser


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': 'Input ID.'},
        max_length=32, label="User ID")
    password = forms.CharField(
        error_messages={'required': 'Input Password.'},
        widget=forms.PasswordInput, label="Password")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                bkuser = Bkuser.objects.get(username=username)
            except Bkuser.DoesNotExist:
                self.add_error('username', 'No ID found.')
                return

            if not check_password(password, bkuser.password):
                self.add_error('password', 'Password is wrong.')
            else:
                self.user_id = bkuser.id

