from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):

    name = request.data['name']
    email = request.data['email']
    password = request.data['password']

    if User.objects.filter(username=email).exists():

        User.objects.create_user(
            username = email,
            password = password,
            first_name = name
        )

        response_data = {
            "status_code" : 6000,
            "message" : "hello"
        }
    else:
            
        response_data = {
            "status_code" : 6001,
            "message" : "this username already exist"
        }
        return Response(response_data)

