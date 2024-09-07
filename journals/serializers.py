"""
journals/serializers
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import JournalEntry, Tag, Category


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


class TagSerializer(serializers.ModelSerializer):
    """
    TagSerializer
    """
    class Meta:
        model = Tag
        fields = ('id', 'tag_name', 'entries',)


class CategorySerializer(serializers.ModelSerializer):
    """
    CategorySerializer
    """
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'user', 'entries')

class JournalEntryCategoryUpdateSerializer(serializers.ModelSerializer):
    """
    JournalEntryCategoryUpdateSerializer
    """
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = JournalEntry
        fields = ('category')