from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('registration', views.registration, name='registration'),
    path('user-cart', views.user_cart, name='user_cart'),
    path('logout/', views.logout, name='logout'),
]
