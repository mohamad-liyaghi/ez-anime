from django import forms
from authentication.models import User


class RegisterUserForm(forms.ModelForm):
    '''A form for creating users'''

    class Meta:
        model = User
        fields = ('email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        user.save()
        return user
