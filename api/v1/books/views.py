from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.books.serializers import BookSerializer
from books.models import Book


@api_view(['GET'])
def books(request):
    instances = Book.objects.filter(is_deleted=False)
    context = {
        "request" : request
    }
    serializer = BookSerializer(instances, many=True,context=context)
    response_data = {
        "status_code" : 6000,
        "data" : serializer.data
    }
    return Response(response_data)


@api_view(['GET'])
def book(request, pk):
    if Book.objects.filter(pk=pk).exists():

        instance = Book.objects.get(pk=pk)
        context = {
            "request" : request
        }
        serializer = BookSerializer(instance,context=context)
        response_data = {
            "status_code" : 6000,
            "data" : serializer.data
        }
        return Response(response_data)
    else:
         response_data = {
            "status_code" : 6000,
            "message" : "This Book Doesn't Exist"
        }