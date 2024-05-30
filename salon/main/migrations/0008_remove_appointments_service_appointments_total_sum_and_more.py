# Generated by Django 4.2.7 on 2024-05-27 16:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_services_duration_mastercategory'),
        ('main', '0007_remove_appointments_date_remove_appointments_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='service',
        ),
        migrations.AddField(
            model_name='appointments',
            name='total_sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Итоговая сумма'),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время'),
        ),
        migrations.CreateModel(
            name='AppointmentService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.appointments', verbose_name='Заявка')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Услуга бронирования',
                'verbose_name_plural': 'Услуги бронирования',
            },
        ),
    ]
