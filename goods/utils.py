from .models import Products
from django.db.models import Q, Value

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


def search(query):
    if query.isdigit():
        return Products.objects.filter(id=int(query))
    
    # Фильтр по средствам джанго 
    vector = SearchVector("title", "description")
    query = SearchQuery(query)

    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

    # Мой фильтр 
    # query_words = [word for word in query.split() if len(word) > 2]
    # q_objects = Q()
    # for word in query_words:
    #     q_objects |= Q(description__icontains=word)
    #     q_objects |= Q(title__icontains=word)

    # return Products.objects.filter(q_objects)




