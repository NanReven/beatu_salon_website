from django.db import models
from services.models import Services
from masters.models import Masters
from masters.models import Users


class Appointments(models.Model):
    class AppointmentStatus(models.TextChoices):
        DECLINED = '0', 'Отклонено'
        ACCEPTED = '1', 'Принято'
        WAITING = '2', 'Ожидает ответ'

    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время начала')
    master = models.ForeignKey(Masters, on_delete=models.DO_NOTHING, verbose_name='Мастер')
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, verbose_name='Посетитель')
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, verbose_name='Услуга')
    status = models.CharField(verbose_name='Статус заявки', max_length=20,
                              choices=AppointmentStatus.choices, default=AppointmentStatus.WAITING)

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'

    def __str__(self):
        return f"{self.master.user.last_name} {self.service} {self.date}"