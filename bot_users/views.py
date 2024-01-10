from django.shortcuts import render
from .models import BotUser

def all_films(request):
    placeholder = ' hu'
    return render(request, 'placeholder')
