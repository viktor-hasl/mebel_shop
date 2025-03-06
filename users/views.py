from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse

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
            if user:
                # Если есть то входим и делаем перевод на другую страницу
                auth.login(request, user)
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

    context = {
        'title' : 'Страница пользователя',
        "form": form,
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

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))