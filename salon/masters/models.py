from django.db import models


class Categories(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    title = models.CharField('Категория', max_length=50)
    photo = models.ImageField('Фотография', upload_to='images/')
    slug = models.SlugField('URL', max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Masters(models.Model):
    master_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField('Имя', max_length=25)
    second_name = models.CharField('Фамилия', max_length=25)
    category_id = models.ForeignKey(Categories,  on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    photo = models.ImageField('Фотография', upload_to='images/')
    email = models.CharField('Почта', max_length=50)
    short_description = models.CharField('Краткая информация', max_length=200)
    full_description = models.TextField('Полная информация')
    rating = models.PositiveIntegerField('Рейтинг', blank=True)
    slug = models.SlugField('URL', max_length=50, unique=True, db_index=True)

    def __str__(self):
        return f"{self.first_name} + {self.second_name}"

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
