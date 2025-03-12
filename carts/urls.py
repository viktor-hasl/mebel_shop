from django.urls import path

from carts import views


app_name = "carts"

urlpatterns = [
    path("cart_remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("cart_add/<slug:product_slug>/", views.cart_add, name="cart_add"),
    path("cart_change/<slug:product_slug>/", views.cart_change, name="cart_change"),
]