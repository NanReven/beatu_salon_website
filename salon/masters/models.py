from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class Position(models.Model):
    title = models.CharField(verbose_name='Должность', max_length=25)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Users(AbstractUser):
    email = models.EmailField(verbose_name='Почта', max_length=50, unique=True, db_index=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Masters(models.Model):
    user: Users = models.OneToOneField(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    position = models.ForeignKey(Position,  on_delete=models.PROTECT, verbose_name='Должность')
    short_description = models.CharField(verbose_name='Краткая информация', max_length=200)
    full_description = models.TextField(verbose_name='Полная информация')
    photo = models.ImageField(verbose_name='Фотография', upload_to='images/')
    admission_date = models.DateField(verbose_name='Дата приема', auto_now_add=True)
    rating = models.PositiveIntegerField(verbose_name='Рейтинг', null=True, blank=True, default=0)
    salary = models.DecimalField(verbose_name='Зарплата', max_digits=8, decimal_places=2)
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True, db_index=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        # Automatically set the slug based on user's first_name and last_name
        self.slug = slugify(f"{self.user.first_name} {self.user.last_name}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'