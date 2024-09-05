"""
journals/views
"""
from rest_framework import generics

from .models import JournalEntry
from .serializers import JournalEntrySerializer


class JournalEntryList(generics.ListCreateAPIView):
    """
    JournalEntryList
    """
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer


class JournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    JournalEntryDetail
    """
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
