from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, username):
    you = get_object_or_404(User, username=username)
    me = request.user                     
                   
    if me.followings.filter(username=username).exists():
        me.followings.remove(you)   
        
    else:
        me.followings.add(you)
    serializer = UserSerializer(me)
    return Response(serializer.data)
    
