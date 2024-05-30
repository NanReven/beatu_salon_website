from django.db import models
from django.utils.timezone import localtime, now

from services.models import Services
from masters.models import Masters
from masters.models import Users


class Appointments(models.Model):
    class AppointmentStatus(models.TextChoices):
        DECLINED = '0', 'Отклонено'
        ACCEPTED = '1', 'Принято'
        WAITING = '2', 'Ожидает ответ'

    start_datetime = models.DateTimeField(verbose_name='Дата и время начала работы', default=now)
    end_datetime = models.DateTimeField(verbose_name='Окончание работы', null=True, blank=True, default=now)
    master = models.ForeignKey(Masters, on_delete=models.DO_NOTHING, verbose_name='Мастер')
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, verbose_name='Посетитель')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    status = models.CharField(verbose_name='Статус заявки', max_length=20,
                              choices=AppointmentStatus.choices, default=AppointmentStatus.WAITING)
    total_sum = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Итоговая сумма')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        local_datetime = localtime(self.start_datetime)
        return f"{self.master.user.last_name} {local_datetime.date()}"


class AppointmentService(models.Model):
    appointment = models.ForeignKey(Appointments, on_delete=models.CASCADE, verbose_name='Заявка')
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, verbose_name='Услуга')

    def __str__(self):
        local_datetime = localtime(self.appointment.start_datetime)
        return f"{self.service.title} {local_datetime.date()}"

    class Meta:
        verbose_name = 'Услуга бронирования'
        verbose_name_plural = 'Услуги бронирования'