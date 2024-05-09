from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# 라우터 생성
router = DefaultRouter()
router.register(r'users', UserViewSet)

# URLConf
urlpatterns = [
    path('', include(router.urls)),
]