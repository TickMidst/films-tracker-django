from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films_library/', include('films_library.urls')),
    path('', include('films_library.urls')),
    path('api/', include('api.urls')),
]
