from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password

from .models import Users
from .models import Appointments
from django.forms import ModelForm


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))


class UserRegistrationForm(ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                'required': True, 'type': 'password', }))

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
            raise forms.ValidationError("Данный адрес уже используется")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        if password2:
            validate_password(password2)
        return cleaned_data

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 17:
            raise forms.ValidationError("Номер телефона ошибочен")
        return phone_number

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.replace('-', '').replace(' ', '').isalpha():
            raise forms.ValidationError("Имя может содержать только буквы, дефисы и пробелы")
        if len(first_name) < 2:
            raise forms.ValidationError("Имя слишком короткое")
        if len(first_name) > 50:
            raise forms.ValidationError("Имя слишком длинное")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.replace('-', '').replace(' ', '').isalpha():
            raise forms.ValidationError("Фамилия может содержать только буквы, дефисы и пробелы")
        if len(last_name) < 2:
            raise forms.ValidationError("Фамилия слишком короткая")
        if len(last_name) > 50:
            raise forms.ValidationError("Фамилия слишком длинная")
        return last_name

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['date', 'time', 'master', 'service']
        labels = {
            'date': 'Дата',
            'time': 'Время начала',
            'master': 'Мастер',
            'service': 'Услуга'
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'id_date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'format': '%H:%M:%S',
                                           'id': 'id_time'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }




