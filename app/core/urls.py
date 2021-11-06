from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register('view/', views.EchoViewSet, base_name='view')

urlpatterns = [
    path('api/<name>/details/', views.EchoApiView.as_view()),
    path('', include(router.urls))
]
