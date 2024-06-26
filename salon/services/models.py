from django.db import models
from masters.models import Masters


class Categories(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=50)
    description = models.TextField(verbose_name='Описание', default="")
    photo = models.ImageField(verbose_name='Фотография', upload_to='images/')
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class MasterCategory(models.Model):
    master = models.ForeignKey(Masters, on_delete=models.PROTECT, null=True, verbose_name='Мастер')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.master.user.last_name + ' ' + self.category.title

    class Meta:
        verbose_name = 'Категории мастеров'
        verbose_name_plural = 'Категории мастеров'


class Services(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, verbose_name='Категория')
    duration = models.TimeField(verbose_name='Длительность')
    cost = models.DecimalField(verbose_name='Стоимость', max_digits=5, decimal_places=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
