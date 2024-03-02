from django.db import models


class Categories(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=50)
    photo = models.ImageField(verbose_name='Фотография', upload_to='images/')
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Services(models.Model):
    title = models.CharField(verbose_name='Название', max_length=20)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    duration = models.DurationField(verbose_name='Длительность')
    cost = models.DecimalField(verbose_name='Стоимость', max_digits=5, decimal_places=0)
    photo = models.ImageField(verbose_name='Фотография', upload_to='images/')
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
