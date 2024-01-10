from films_library.models import Film, Category
from bot_users.models import BotUser
from rest_framework import viewsets
from .serializers import CategorySerializer, FilmSerializer, BotUserSerializer
from rest_framework.pagination import PageNumberPagination


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class LastFilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = SmallResultsSetPagination


class BadFilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.filter(category=1)
    serializer_class = FilmSerializer


class GoodFilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.filter(category=2)
    serializer_class = FilmSerializer
    

class BotUserViewSet(viewsets.ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
