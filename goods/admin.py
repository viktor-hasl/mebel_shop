from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']

    # Автозаполнение slug
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'count', 'category', 'discount', 'img']
    list_editable = ['count', 'category', 'img', 'discount']
    prepopulated_fields = {'slug': ('title',)}
