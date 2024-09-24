"""
journals/urls
"""
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from rest_framework.routers import DefaultRouter

from journals import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'entries', views.JournalEntryViewSet, basename='entries')
router.register(r'tags', views.TagViewSet, basename='tags')
router.register(r'categories', views.CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema')
]
