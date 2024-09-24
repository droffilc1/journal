"""
Admin
"""
from django.contrib import admin

from .models import JournalEntry, Tag, Category

admin.site.register(JournalEntry)
admin.site.register(Tag)
admin.site.register(Category)
