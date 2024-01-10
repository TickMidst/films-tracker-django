from django.contrib import admin
from .models import BotUser


class BotUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'created_at')


admin.site.register(BotUser, BotUserAdmin)
