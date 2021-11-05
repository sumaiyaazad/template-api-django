from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
# router.register('user', views.UserViewSet)
router.register('hello', views.HelloViewSet, base_name='hello')

# app_name = 'hi'

urlpatterns = [
    path('', include(router.urls))
]
