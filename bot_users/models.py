from django.db import models
from django.utils import timezone


class BotUser(models.Model):
    user_id = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user_id)
