from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

current_year = datetime.now().year


class Category(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    year = models.PositiveBigIntegerField(
        validators=[MinValueValidator(2021), MaxValueValidator(current_year)]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.title
