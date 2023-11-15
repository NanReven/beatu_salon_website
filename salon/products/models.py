from django.db import models


class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    title = models.CharField('Название', max_length=20)
    quantity = models.PositiveIntegerField('Количество')
    slug = models.SlugField('URL', max_length=50, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.title
