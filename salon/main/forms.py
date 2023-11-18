from .models import Users
from django.forms import ModelForm, TextInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'second_name', 'email', 'password']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'text'
            }),
            'second_name': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'text'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'email'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'type': 'password'
            })
        }
