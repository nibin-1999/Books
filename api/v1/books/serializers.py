from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from books.models import Comment, Book


class BookSerializer(ModelSerializer):
    
    categories=serializers.SerializerMethodField()
    class Meta:
        model=Book
        fields="__all__"

    def get_categories(self, instance):
        return [category.name for category in instance.categories.all()]

class CommentSerializer(ModelSerializer):
    class Meta:
        fields =("id","user","comment","date")
        model = Comment