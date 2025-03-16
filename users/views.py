import decimal
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

# Create your views here.


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        # Проверяем на валидность
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            # Проверяем или есть такой пользователь
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                # Если есть то входим и делаем перевод на другую страницу
                auth.login(request, user)
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"title": "Авторизация", "form": form}

    return render(request, "users/login.html", context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные изменены')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
    
    orders = Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id")
    
    total_price = {}
    for order in orders:
        total_price[order.id]  = 0.00
    
        for item in order.orderitem_set.all():
            total_price[order.id] += float(item.products_price())
            
            
        
    context = {
        'title' : 'Страница пользователя',
        "form": form,
        'orders': orders,
        'total_price': total_price
    }
    return render(request, "users/profile.html", context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {"title": "Регистарция", 'form': form}

    return render(request, "users/registration.html", context)

def user_cart(request):
    context = {
        'title':'Корзина'
    }
    return render(request, 'users/users_cart.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))