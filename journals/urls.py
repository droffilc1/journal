"""
journals/urls
"""
from rest_framework.routers import DefaultRouter

from journals import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'journals', views.JournalEntryViewSet, basename='journals')
router.register(r'tags', views.TagViewSet, basename='tags')

urlpatterns = router.urls
