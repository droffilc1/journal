"""
journals/views
"""
from rest_framework import generics

from .models import JournalEntry
from .permissions import IsAuthOrReadOnly
from .serializers import JournalEntrySerializer


class JournalEntryList(generics.ListCreateAPIView):
    """
    JournalEntryList
    """
    permission_classes = (IsAuthOrReadOnly,)
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer


class JournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    JournalEntryDetail
    """
    permission_classes = (IsAuthOrReadOnly,)
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
