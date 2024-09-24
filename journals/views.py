"""
journals/views
"""
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import JournalEntry, Tag, Category
from .permissions import IsAuthOrReadOnly
from .serializers import JournalEntrySerializer, UserSerializer,\
      TagSerializer, CategorySerializer, JournalEntryCategoryUpdateSerializer


class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    JournalEntryViewSet
    """
    permission_classes = (IsAuthOrReadOnly,)
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('title', 'content')

    @action(detail=False, methods=['get'])
    def filter_by_tag(self, request):
        """
        Filter Entries by Tag
        """
        tag_name = request.query_params.get('tag_name', None)
        if tag_name:
            tag = Tag.objects.filter(name=tag_name).first()
            if tag:
                entries = JournalEntry.objects.filter(tags=tag)
                serializer = self.get_serializer(entries, many=True)
                return Response(serializer.data)
            return Response({'detail': 'Tag not found'}, status=404)
        return Response({"detail": "Tag query parameter is required."},
                        status=400)

    @action(detail=True, methods=['patch'])
    def category(self, request, pk=None):
        """
        Assign Category to Entry
        """
        entry = self.get_object()
        serializer = JournalEntryCategoryUpdateSerializer(
            entry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search Entries
        """
        query = request.query_params.get('q', None)
        if query:
            entries = JournalEntry.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
            serializer = self.get_serializer(entries, many=True)
            return Response(serializer.data)
        return Response({"detail": "Query parameter is required."}, status=400)


class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet
    """
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    TagViewSet
    """
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    CategorySet
    """
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
