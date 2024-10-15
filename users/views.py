from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import UserProfile

from users.serializers import UserProfileSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all code user profiles, or create a new profile.
    """
    if request.method == 'GET':
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code user profile.
    """
    try:
        user = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
