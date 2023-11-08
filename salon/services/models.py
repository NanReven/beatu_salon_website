from django.db import models
from masters.models import Speciality


class Services(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    title = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=250)
    duration = models.DurationField('Длительность')
    cost = models.DecimalField('Стоимость', max_digits=6, decimal_places=2)
    photo = models.ImageField('Фотография', upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServiceSpeciality(models.Model):
    service_id = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Услуга-Специальность'
        verbose_name_plural = 'Услуга-Специальность'


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    title = models.CharField('Название', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CategoryService(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    service_id = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Категория-Услуга'
        verbose_name_plural = 'Категория-Услуга'