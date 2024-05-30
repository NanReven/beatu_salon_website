# Generated by Django 4.2.7 on 2024-05-29 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_appointments_service_appointments_total_sum_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='datetime',
        ),
        migrations.AddField(
            model_name='appointments',
            name='end_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Окончание работы'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='start_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время начала работы'),
        ),
    ]