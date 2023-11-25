from rest_framework.serializers import ModelSerializer
from books.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        fields = ("title","featured_image","author","categories","rating","comments","is_favourite","is_deleted")
        model = Book



class BookDetailSerializer(ModelSerializer):
    class Meta:
        fields = ("title","featured_image","author","categories","rating","comments","is_favourite","is_deleted")
        model = Book