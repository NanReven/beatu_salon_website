# Generated by Django 4.2.7 on 2024-02-29 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masters', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masters.masters', verbose_name='Мастер'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.services', verbose_name='Услуга'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Посетитель'),
        ),
    ]
