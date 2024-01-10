from django.contrib import admin
from .models import Film, Category

admin.site.site_header = 'Films Tracker Admin'
admin.site.site_title = 'Films'
admin.site.index_title = 'Welcome to the Films Tracker Admin Area'


class FilmsInline(admin.TabularInline):
    model = Film
    extra = 1


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']})
    ]
    inlines = [FilmsInline]


admin.site.register(Film, FilmAdmin)
admin.site.register(Category, CategoryAdmin)
