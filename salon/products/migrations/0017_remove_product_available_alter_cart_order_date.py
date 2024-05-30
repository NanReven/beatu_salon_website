# Generated by Django 4.2.7 on 2024-05-29 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_cart_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 15, 31, 48, 455533), verbose_name='Дата оформления'),
        ),
    ]
