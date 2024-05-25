import datetime as datetime
from django.db import models
from django.utils.timezone import localtime

from services.models import Services
from masters.models import Masters
from masters.models import Users


class Appointments(models.Model):
    class AppointmentStatus(models.TextChoices):
        DECLINED = '0', 'Отклонено'
        ACCEPTED = '1', 'Принято'
        WAITING = '2', 'Ожидает ответ'

    datetime = models.DateTimeField(verbose_name='Дата и время', default=datetime.datetime.now())
    master = models.ForeignKey(Masters, on_delete=models.DO_NOTHING, verbose_name='Мастер')
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, verbose_name='Посетитель')
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, verbose_name='Услуга')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    status = models.CharField(verbose_name='Статус заявки', max_length=20,
                              choices=AppointmentStatus.choices, default=AppointmentStatus.WAITING)

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'

    def __str__(self):
        local_datetime = localtime(self.datetime)
        return f"{self.master.user.last_name} {self.service} {local_datetime.date()}"