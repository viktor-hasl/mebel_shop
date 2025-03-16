import email
from django.contrib import admin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User
# Register your models here.

@admin.register(User)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['email', 'username', 'last_name']

    inlines = [CartTabAdmin, OrderTabulareAdmin]