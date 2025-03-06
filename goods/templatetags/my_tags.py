from django.utils.http import urlencode

from goods.models import Categories

from django import template

register = template.Library()


@register.simple_tag()
def get_category():
    category = Categories.objects.all()
    return category


# С помощью его мы делаем так, чтобы фильтр не сбрасывался при переходе на другую страницу
@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)