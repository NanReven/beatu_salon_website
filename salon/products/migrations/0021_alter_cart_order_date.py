# Generated by Django 4.2.7 on 2024-06-18 12:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_cart_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата оформления'),
        ),
    ]
