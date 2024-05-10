from django.urls import path, include
from rest_framework.routers import DefaultRouter

# 라우터 생성


# URLConf
urlpatterns = [
    path('user', views.index),
]