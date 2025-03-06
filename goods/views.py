from django.shortcuts import render, get_list_or_404
from goods.models import Products, Categories
from django.core.paginator import Paginator

from .utils import search


# Create your views here.


def catalog(request, catalog_slug=None):
    on_sale = request.GET.get("on_sale")
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)
    if catalog_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = search(query)
    else:
        # category = Categories.objects.get(slug=catalog_slug)
        # goods = Products.objects.filter(category=category)
        goods = Products.objects.filter(category__slug=catalog_slug)
    if on_sale:
        goods = goods.filter(discount__gt=0.0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    content = {"title": "Каталог", "goods": page_obj, "catalog_slug": catalog_slug}
    return render(request, "goods/catalog.html", content)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    content = {"title": "Продукт", "product": product}

    return render(request, "goods/product.html", content)


# Добавлял товар в бд
# def add_category_and_products(request):
#     # x = Categories(name='Все товары')
#     # x.save()
#     # x = Categories(name='Кухня')
#     # x.save()
#     # x = Categories(name='Спальня')
#     # x.save()
#     # x = Categories(name='Гостинная')
#     # x.save()
#     # x = Categories(name='Офис')
#     # x.save()
#     # x = Categories(name='Фурнитура')
#     # x.save()
#     # x = Categories(name='Декор')
#     # x.save()
#     products = [{
#     "image": "deps/images/goods/set of tea table and three chairs.jpg",
#     "name": "Чайный столик и три стула",
#     "description": "Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.",
#     "price": 150.00
#   },
#   {
#     "image": "deps/images/goods/set of tea table and two chairs.jpg",
#     "name": "Чайный столик и два стула",
#     "description": "Набор из стола и двух стульев в минималистическом стиле.",
#     "price": 93.00
#   },
#   {
#     "image": "deps/images/goods/double bed.jpg",
#     "name": "Двухспальная кровать",
#     "description": "Кровать двухспальная с надголовником и вообще очень ортопедичная.",
#     "price": 670.00
#   },
#   {
#     "image": "deps/images/goods/kitchen table.jpg",
#     "name": "Кухонный стол с раковиной",
#     "description": "Кухонный стол для обеда с встроенной раковиной и стульями.",
#     "price": 365.00
#   },
#   {
#     "image": "deps/images/goods/kitchen table 2.jpg",
#     "name": "Кухонный стол с встройкой",
#     "description": "Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.",
#     "price": 430.00
#   },
#   {
#     "image": "deps/images/goods/corner sofa.jpg",
#     "name": "Угловой диван для гостинной",
#     "description": "Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!",
#     "price": 610.00
#   },
#   {
#     "image": "deps/images/goods/bedside table.jpg",
#     "name": "Прикроватный столик",
#     "description": "Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).",
#     "price": 55.00
#   },
#   {
#     "image": "deps/images/goods/sofa.jpg",
#     "name": "Диван обыкновенный",
#     "description": "Диван, он же софа обыкновенная, ничего примечательного для описания.",
#     "price": 190.00
#   },
#   {
#     "image": "deps/images/goods/office chair.jpg",
#     "name": "Стул офисный",
#     "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
#     "price": 30.00
#   },
#   {
#     "image": "deps/images/goods/plants.jpg",
#     "name": "Растение",
#     "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
#     "price": 10.00
#   },
#   {
#     "image": "deps/images/goods/flower.jpg",
#     "name": "Цветок стилизированный",
#     "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
#     "price": 15.00
#   },
#   {
#     "image": "deps/images/goods/strange table.jpg",
#     "name": "Прикроватный столик",
#     "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
#     "price": 25.00
#   }]
#     for product in products:
#         x = Products(title=product['name'], description=product['description'], category_id=3, price=product['price'])
#         x.save()
