"""
journals/views
"""
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import JournalEntry, Tag
from .permissions import IsAuthOrReadOnly
from .serializers import JournalEntrySerializer, UserSerializer, TagSerializer


class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    JournalEntryViewSet
    """
    permission_classes = (IsAuthOrReadOnly,)
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet
    """
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    TagViewSet
    """
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
