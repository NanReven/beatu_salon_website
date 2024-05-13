# Generated by Django 4.2.7 on 2024-05-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cart_cartitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Товары корзин', 'verbose_name_plural': 'Товары корзин'},
        ),
        migrations.AddField(
            model_name='cart',
            name='issue_code',
            field=models.CharField(default='0000', max_length=4, verbose_name='Код выдачи'),
        ),
    ]