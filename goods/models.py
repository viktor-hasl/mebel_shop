from django.db import models
from django.urls import reverse

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} id: {self.pk}'


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')
    img = models.ImageField(upload_to='media_goods/', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    count = models.PositiveIntegerField(default=0, verbose_name='Количество')
    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name='Скидка в процентах')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("goods:product", kwargs={"product_slug": self.slug})
    

    def redone_index(self):
        return f"{self.pk:05}"

    def math_discount(self):
        if self.discount:
            return round(self.price - (self.price * self.discount) / 100, 2)
        return self.price