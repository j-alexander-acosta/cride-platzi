"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
<<<<<<< HEAD
    path('', include(router.urls)),
]
=======
    path('', include(router.urls))
]
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
