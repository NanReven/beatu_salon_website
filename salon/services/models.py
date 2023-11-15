from django.db import models
from masters.models import Categories


class Services(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    title = models.CharField('Название', max_length=20)
    category_id = models.ForeignKey(Categories,  on_delete=models.SET_NULL, null=True,  verbose_name='Категория')
    description = models.TextField('Описание')
    duration = models.DurationField('Длительность')
    cost = models.DecimalField('Стоимость', max_digits=5, decimal_places=0)
    photo = models.ImageField('Фотография', upload_to='images/')
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
