from Profiles.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions, status, viewsets

# Create your views here.
@api_view(['GET'])
def activate_social(request):
    user = request.user
    user.social_active = True
    user.social_count = 0
    user.save()

    serializer = UserDetailSerializer(request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def deactivate_social(request):
    user = request.user
    user.social_active = False
    user.social_count = 0
    user.save()

    serializer = UserDetailSerializer(request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)