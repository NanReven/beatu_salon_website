# Generated by Django 4.2.7 on 2024-05-12 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_cart_order_date_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Сумма заказа'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 23, 53, 58, 728327), verbose_name='Дата оформления'),
        ),
    ]
