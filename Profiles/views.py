from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from datetime import datetime, timezone

from .models import *

from .serializers import *

# time delta
td = 30

class AuthView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, email=self.request.user.email)
        return obj

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserDetailSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
def notify(request):

    remind = False
    serializer = UserDetailSerializer(request.user)

    if(serializer.data['timer_active']):
        remind = ( datetime.now() - datetime.strptime(serializer.data['timer_last_active'], '%Y-%m-%dT%H:%M:%S.%fZ') ).total_seconds() / 60 > 1

        if(remind):
            user = request.user
            user.timer_last_active = datetime.now()
            user.save()
        
        return Response({'remind': remind})

    return Response({'remind': remind})

@api_view(['GET'])
def activate_reminder(request):
    user = request.user
    user.timer_active = True
    user.timer_last_active = datetime.now()
    user.save()

    serializer = UserDetailSerializer(request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def deactivate_reminder(request):
    user = request.user
    user.timer_active = False
    user.save()

    serializer = UserDetailSerializer(request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)
