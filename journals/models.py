"""
journals/models
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
        - is_draft: Boolean indicating whether the entry is
                     a draft or published.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user}: {self.title}"

class Tag(models.Model):
    """
    Tag Model
      Attributes:
        - name: The name of the tag.
        - entries: Many-to-many relationship with JournalEntry to allow
                   multiple tags per entry.
    """
    name = models.CharField(max_length=50)
    entries = models.ManyToManyField(JournalEntry)

    def __str__(self) -> str:
        return f"{self.name}"
