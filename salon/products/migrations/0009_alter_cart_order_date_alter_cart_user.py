# Generated by Django 4.2.7 on 2024-05-12 10:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_alter_cart_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 13, 13, 33, 359666), verbose_name='Дата оформления'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
