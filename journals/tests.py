"""
Tests
"""
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import JournalEntry, Tag, Category


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
        self.assertEqual(str(self.journal), 'testuser: A good title')


class TagTests(TestCase):
    """
    TagTests
    """
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(tag_name='Test Tag')

    def test_tag_model(self):
        self.assertEqual(self.tag.tag_name, 'Test Tag')
        self.assertEqual(str(self.tag), 'Test Tag')
        self.assertEqual(self.tag.entries.count(), 0)
        self.assertQuerySetEqual(self.tag.entries.all(), [])

class CategoryTests(TestCase):
    """
    CategoryTests
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='secret',
        )
        cls.category = Category.objects.create(
            category_name='Test Category',
            user=cls.user
        )

    def test_category_model(self):
        self.assertEqual(self.category.category_name, 'Test Category')
        self.assertEqual(str(self.category), 'Test Category')

