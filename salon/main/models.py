from django.db import models
from masters.models import Masters


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField('Имя', max_length=25)
    second_name = models.CharField('Фамилия', max_length=25)
    email = models.CharField('Почта', max_length=50)
    phone = models.CharField('Телефон', max_length=11)
    password = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Appointments(models.Model):
    appointment_id = models.BigAutoField(primary_key=True)
    date = models.DateField('Дата')
    time = models.DateTimeField('Время начала')
    master_id = models.ForeignKey(Masters, on_delete=models.SET_NULL, null=True, verbose_name='Мастер')
    user_id = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, verbose_name='Посетитель')

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'
