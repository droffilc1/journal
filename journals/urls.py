"""
journals/urls
"""
from rest_framework.routers import SimpleRouter

from .views import JournalEntryViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', JournalEntryViewSet, basename='journals')

urlpatterns = router.urls
