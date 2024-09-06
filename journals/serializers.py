"""
journals/serializers
"""
from django.contrib.auth import get_user_model
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


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer
    """
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
