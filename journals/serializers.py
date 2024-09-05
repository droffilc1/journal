"""
journals/serializers
"""
from rest_framework import serializers

from .models import JournalEntry


class JournalEntrySerializer(serializers.ModelSerializer):
    """
    JournalEntrySerializer
    """
    class Meta:
        model = JournalEntry
        fields = (
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'is_draft',
        )
