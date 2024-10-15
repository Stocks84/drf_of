from django.contrib.auth.models import User
from rest_framework import serializers, permissions, viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from users.models import UserProfile

from users.serializers import UserProfileSerializer

# Create your views here.


@csrf_exempt
def user_list(request):
    """
    List all code user profiles, or create a new profile.
    """
    if request.method == 'GET':
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=false)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
