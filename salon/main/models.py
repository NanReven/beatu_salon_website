from django.db import models
from services.models import Services
from masters.models import Masters
from masters.models import Users


class Appointments(models.Model):
    date = models.DateField(verbose_name='Дата')
    time = models.DateTimeField(verbose_name='Время начала')
    master = models.ForeignKey(Masters, on_delete=models.DO_NOTHING, verbose_name='Мастер')
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, verbose_name='Посетитель')
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, verbose_name='Услуга')
    ## cost ?

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'
