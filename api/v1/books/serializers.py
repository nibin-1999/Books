from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from books.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        fields = ("title","featured_image","author","categories","is_favourite")
        model = Book



class BookDetailSerializer(ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        fields = ("title","featured_image","author","categories","rating","comments","is_favourite","is_deleted")
        model = Book

    def get_category(self, instance):
        return instance.category.name