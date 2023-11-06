from django.db import models


class Masters(models.Model):
    master_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Фамилия', max_length=50)
    photo = models.ImageField('Фотография', upload_to='images/')
    short_description = models.CharField('Краткая информация', max_length=200)
    full_description = models.TextField('Полная информация')
    rating = models.PositiveIntegerField('Рейтинг')


class Speciality(models.Model):
    speciality_id = models.BigAutoField(primary_key=True)
    speciality = models.CharField('Специальность', max_length=50)


class MasterSpeciality(models.Model):
    master_id = models.ForeignKey(Masters, on_delete=models.SET_NULL, null=True)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True)
