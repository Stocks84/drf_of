from users.models import UserProfile
from users.serializers import UserProfileSerializer
from rest_framework import generics
# from django.http import Http404 
# from rest_framework.views import APIView 
# from rest_framework.response import Response
# from rest_framework import status
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# class UserList(APIView):
#     """
#     List all user profiles, or create a new profile.
#     """
#     def get(self, request, format=None):
#         users = UserProfile.objects.all()
#         serializer = UserProfileSerializer(users, many=True)
#         return Response(serializer.data)

#     def post (self, request, formant=None):
#         serializer = UserProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserDetail(APIView):
#     """
#     Retrieve, update or delete a code user profile.
#     """
#     def get_object(self, pk):
#         try:
#             return UserProfile.objects.get(pk=pk)
#         except UserProfile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserProfileSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserProfileSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request,pk, format=None):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

