from django.urls import path

from goods import views


app_name = "goods"

urlpatterns = [
    path("<slug:catalog_slug>/", views.catalog, name="catalog"),
    path("search/", views.catalog, name="search"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
