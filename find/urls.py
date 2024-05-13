from django.urls import path
from .views import VisitorAPIView

urlpatterns = [
    path('visitors/', VisitorAPIView.as_view(), name='visitor_api'),
]