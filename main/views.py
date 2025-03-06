from django.shortcuts import render, HttpResponse
from goods.models import Categories

# Create your views here.


def index(request):

    context = {"title": "Meбель - Главная страница", "content": "Магазин мебели HOME!"}
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "About: страница о нас",
        "content": "О нас ",
        "content_text": "Текст рассказывает о том какой хороший магазин и кто они такие ",
    }
    return render(request, "main/about.html", context)
