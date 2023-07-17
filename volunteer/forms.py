from django import forms
from django.contrib.auth.models import User


class VolunteerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
