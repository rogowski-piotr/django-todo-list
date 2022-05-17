from django.urls import include, path
from rest_framework import routers
from .views import HeroView, TodoView, UserView, check_credentials


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'heroes', HeroView)
router.register(r'todos', TodoView)
router.register(r'users', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', check_credentials, name='post_val'),
]