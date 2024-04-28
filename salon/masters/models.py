from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from unidecode import unidecode
from django.template.defaultfilters import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class Position(models.Model):
    title = models.CharField(verbose_name='Должность', max_length=25)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Users(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Почта', max_length=50, unique=True, db_index=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, unique=True)
    is_customer = models.BooleanField(verbose_name='Клиент', default=True, help_text='Уберите отметку, '
                                                                        'если пользователь является сотрудником салона')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

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
        msg = f"{self.user.first_name} {self.user.last_name}"
        self.slug = slugify(unidecode(msg))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'