"""
Admin
"""
from django.contrib import admin

from .models import JournalEntry, Tag

admin.site.register(JournalEntry)
admin.site.register(Tag)