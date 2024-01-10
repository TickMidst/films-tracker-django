from rest_framework import serializers
from films_library.models import Film, Category
from bot_users.models import BotUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'