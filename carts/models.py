
from django.db import models

from users.models import User
from goods.models import Products
# Create your models here.


class CartQyerySet(models.QuerySet):
    

    def total_price(self):
        return sum(cart.product_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        else:
            return 0

class Cart(models.Model):
    user= models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    create_datatime = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    
    objects = CartQyerySet().as_manager()

    def __str__(self):
        if not self.user:
            username = self.session_key
        else:
            username = self.user.username
        return f'Корзина: {username} | Товар: {self.product} |  Количество: {self.quantity}'
    
    def product_price(self):
        return round(self.product.math_discount() * self.quantity , 2)
    
