"""
Models
"""
from django.conf import settings
from django.db import models


class JournalEntry(models.Model):
    """
    JournalEntry Model
      Attributes:
        - user: Foreign key linking the entry to a user.
        - title: Title of the journal entry.
        - content: The main content of the entry.
        - created_at: Timestamp of when the entry was created.
        - updated_at: Timestamp of the last update.
        - is_draft: Boolean indicating whether the entry is a draft or published.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
