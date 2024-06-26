# Generated by Django 4.2.7 on 2024-05-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0008_alter_users_is_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('ПН', 'Понедельник'), ('ВТ', 'Вторник'), ('СР', 'Среда'), ('ЧТ', 'Четверг'), ('ПТ', 'Пятница'), ('СБ', 'Суббота'), ('ВС', 'Воскресенье')], max_length=20, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='masters',
            name='rating',
        ),
        migrations.AddField(
            model_name='masters',
            name='weekend',
            field=models.ManyToManyField(limit_choices_to=2, to='masters.weekday', verbose_name='Выходные'),
        ),
    ]
