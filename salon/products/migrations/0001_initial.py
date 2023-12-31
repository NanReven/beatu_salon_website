# Generated by Django 4.2.7 on 2023-11-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товар',
            },
        ),
    ]
