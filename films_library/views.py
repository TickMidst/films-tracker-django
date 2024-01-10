from django.shortcuts import render, get_object_or_404
from .models import Film


def all_films(request):
    films = Film.objects.all()
    return render(request, 'films_library/all_films.html', {'films': films})


def bad_films(request):
    films = Film.objects.filter(category=1)
    return render(request, 'films_library/all_films.html', {'films': films})


def good_films(request):
    films = Film.objects.filter(category=2)
    return render(request, 'films_library/all_films.html', {'films': films})


def single_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'films_library/single_film.html', {'film': film})
