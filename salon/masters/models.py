from django.db import models


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category = models.CharField('Категория', max_length=50)
    photo = models.ImageField('Фотография', upload_to='images/')
    slug = models.SlugField('URL', max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Masters(models.Model):
    master_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField('Имя', max_length=25)
    second_name = models.CharField('Фамилия', max_length=25)
    category_id = models.ForeignKey(Category,  on_delete=models.SET_NULL, null=True)
    photo = models.ImageField('Фотография', upload_to='images/')
    short_description = models.CharField('Краткая информация', max_length=200)
    full_description = models.TextField('Полная информация')
    rating = models.PositiveIntegerField('Рейтинг', blank=True)
    slug = models.SlugField('URL', max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.second_name

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
