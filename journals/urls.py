"""
journals/urls
"""
from django.urls import path

from .views import JournalEntryList, JournalEntryDetail

urlpatterns = [
    path('<int:pk>/', JournalEntryDetail.as_view(), name='journal_detail'),
    path('', JournalEntryList.as_view(), name='journal_list'),
]
