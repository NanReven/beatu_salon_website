# Generated by Django 4.2.7 on 2024-05-30 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_cart_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 30, 12, 4, 18, 709168), verbose_name='Дата оформления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='URL'),
        ),
    ]
