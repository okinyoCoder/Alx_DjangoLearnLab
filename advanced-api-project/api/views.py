from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics, serializers,filters
from django_filters import rest_framework
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'publication_year']
    ordering_fields =  ['title', 'publication_year']
    ordering = ['title']

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        title_filter = self.request.query_params.get('title', None)
        if title_filter is not None:
            queryset = queryset.filter(title__icontains=title_filter)
        return queryset

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]