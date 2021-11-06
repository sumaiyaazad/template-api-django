from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()

# router.register('view', views.EchoViewSet, base_name='view')
router.register('view/(?P<name>.+)/details', views.EchoViewSet, base_name='view')
# .as_view({'get': 'retrieve', 'post':'create'})

urlpatterns = [
    path('api/<name>/details', views.EchoApiView.as_view(), name='api'),
    path('', include(router.urls))
]
