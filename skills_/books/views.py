from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from books.models import Book, Author

from books.serializers import AuthorSerializer
from books.serializers import BookSerializer

# Create your views here.
class RetrieveBooks(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        books_list = Book.objects.filter(status=True)#.values()
        serializer = BookSerializer(books_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveAuthors(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        author_list = Author.objects.all()
        serialzer =AuthorSerializer(author_list, many=True)
        return Response(serialzer.data)

class CreateAuthor(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateBook(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveAuthorAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, author_id):
        author_obj = Author.objects.get(id=author_id)
        serialzer = AuthorSerializer(author_obj)
        return Response(serialzer.data)

class RetrieveBookAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, book_id):
        book_obj = get_object_or_404(Book, pk=book_id)
        serialzer = BookSerializer(book_obj)
        return Response(serialzer.data)

    def put(self, request, book_id):
        book_obj = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(instance=book_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, book_id):
        book_obj = get_object_or_404(Book, pk=book_id)
        book_obj.status = False
        book_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
