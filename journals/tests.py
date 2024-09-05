"""
Tests
"""
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import JournalEntry


class JournalTests(TestCase):
    """
    JournalTests
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='secret',
        )

        cls.journal = JournalEntry.objects.create(
            user=cls.user,
            title='A good title',
            content='Nice content',
        )

    def test_journalentry_model(self):
        self.assertEqual(self.journal.user.username, 'testuser')
        self.assertEqual(self.journal.title, 'A good title')
        self.assertEqual(self.journal.content, 'Nice content')
        self.assertEqual(str(self.journal), 'A good title')
