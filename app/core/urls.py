from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register('hello', views.HelloViewSet, base_name='hello-view')

urlpatterns = [
    path('', include(router.urls))
]
