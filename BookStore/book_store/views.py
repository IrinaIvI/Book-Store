from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class BookPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.request.query_params.get('author_id', None)
        if author_id is not None:
            queryset = queryset.filter(author_id=author_id)  
        return queryset

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        if book.count > 0:
            book.count -= 1
            book.save()
            return Response({"message": "Book purchased successfully!"})
        return Response({"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.request.query_params.get('author_id', None)
        if author_id is not None:
            queryset = queryset.filter(id=author_id)
        return queryset
