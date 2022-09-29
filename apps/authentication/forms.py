from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    '''A form for creating users'''

    class Meta:
        model = User
        fields = ('email', 'password')
