from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'list-users': '/users',
        'get-user-by-id': '/users/<int:id>',
        'create-user': '/users/create/',
        'update-user': '/users/update/<int:id>/',
        'delete-user': '/users/delete/<int:id>/',
    }
    return Response(api_urls)

# Create View
@api_view(['POST'])
def create_user(request):
    user_serializer = UserSerializer(data=request.data)
    
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Read View (List all users or get user by ID)
@api_view(['GET'])
def list_or_get_user(request, id=None):
    if id:
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# Update View
@api_view(['PUT'])
def update_user(request, id):
    user = get_object_or_404(User, id=id)
    user_serializer = UserSerializer(instance=user, data=request.data)
    
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete View
@api_view(['DELETE'])
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
