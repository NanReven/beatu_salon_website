from .models import Users
from django.forms import ModelForm, TextInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'text'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'text'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'email'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'phone'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'password',
                'name': 'password'
            })
        }
