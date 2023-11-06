# Generated by Django 4.2.7 on 2023-11-05 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Masters',
            fields=[
                ('master_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('photo', models.ImageField(upload_to='')),
                ('short_description', models.CharField(max_length=200, verbose_name='Краткая информация')),
                ('full_description', models.TextField(verbose_name='Полная информация')),
                ('rating', models.PositiveIntegerField(verbose_name='Рейтинг')),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('speciality_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('speciality', models.CharField(max_length=50, verbose_name='Специальность')),
            ],
        ),
        migrations.CreateModel(
            name='MasterSpeciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='masters.masters')),
                ('speciality_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='masters.speciality')),
            ],
        ),
    ]
