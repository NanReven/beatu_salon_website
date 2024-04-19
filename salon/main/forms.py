from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password

from .models import Users
from django.forms import ModelForm


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))


class UserRegistrationForm(ModelForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True, 'type': 'password'}))

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'text'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'type': 'email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'tel'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': True, 'type': 'password'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        validate_password(password1)  # This line will raise a ValidationError if the password doesn't meet the security requirements
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
