# Generated by Django 4.2.7 on 2024-03-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0002_remove_users_second_name_alter_masters_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masters',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='URL'),
        ),
    ]