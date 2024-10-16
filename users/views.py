from rest_framework import status
from rest_framework.response import Response 
from rest_framework.viewa import APIVIew
from django.contrib.auth.models import User


class SignupView(APIVIew):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if username and password and email:
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)




