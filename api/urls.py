from rest_framework import routers
from api.views import BadFilmViewSet, CategoryViewSet, FilmViewSet, GoodFilmViewSet, LastFilmViewSet, BotUserViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'allfilms', FilmViewSet, basename='allfilms')
router.register(r'lastfilms', LastFilmViewSet, basename='lastfilms')
router.register(r'badfilms', BadFilmViewSet, basename='badfilms')
router.register(r'goodfilms', GoodFilmViewSet, basename='goodfilms')
router.register(r'botusers', BotUserViewSet, basename='botusers')

urlpatterns = router.urls
