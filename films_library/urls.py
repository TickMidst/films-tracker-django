from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.all_films, name='all_films'),
    path('bad_films/', views.bad_films, name='bad_films'),
    path('good_films/', views.good_films, name='good_films'),
    path('<int:film_id>', views.single_film, name='single_film')
]
