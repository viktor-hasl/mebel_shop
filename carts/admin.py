from tabnanny import verbose
from django.contrib import admin
from .models import Cart

# Register your models here.

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'create_datatime'
    search_fields = 'product', 'quantity', 'create_datatime'
    readonly_fields = ('create_datatime',)
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'create_datatime']

    def product(self, obj):
        return str(obj.product.title)
    


