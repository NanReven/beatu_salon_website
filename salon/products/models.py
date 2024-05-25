import datetime

from django.db import models
from masters.models import Users


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Доступен для покупки')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение')
    slug = models.SlugField(verbose_name='URL', max_length=150, unique=True, db_index=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Cart(models.Model):
    class CartStatus(models.TextChoices):
        PENDING = 'pending', 'Ожидает подтверждения'
        READY = 'ready', 'Готов к выдаче'
        CANCELLED = 'canceled', 'Отменен'
        COMPLETED = 'completed', 'Выдан'

    user: Users = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь', unique=False)
    order_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата оформления')
    status = models.CharField(max_length=20, choices=CartStatus.choices, default='pending', verbose_name='Статус заказа')
    issue_code = models.CharField(max_length=4, verbose_name='Код выдачи', default='0000')
    total_sum = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Сумма заказа')

    def __str__(self):
        return f"{self.user.last_name} {self.issue_code}"

    def save(self, *args, **kwargs):
        # Проверяем, изменилось ли значение поля status на 'canceled'
        if self.status == 'canceled':
            for cart_item in CartItem.objects.filter(cart=self.pk):
                product = cart_item.product
                product.quantity += cart_item.quantity
                product.save()

        # Вызываем оригинальный метод save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество товара')

    def __str__(self):
        return f"{self.cart} {self.product}"

    class Meta:
        verbose_name = 'Товары корзин'
        verbose_name_plural = 'Товары корзин'
