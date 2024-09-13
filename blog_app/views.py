from django.shortcuts import render
from django.http import JsonResponse  # Correct import
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

# Create your views here.
def blog_list(request):
    data = {
        "Message": "Hello world"  # Correct dictionary syntax
    }

    return JsonResponse(data)

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
