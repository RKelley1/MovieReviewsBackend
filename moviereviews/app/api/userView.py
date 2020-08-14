from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from moviereviews.app.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from moviereviews.app.api.helpers.validators import validateEmail
# model imports
# from moviereviews.app.models import User

from moviereviews.app.api.helpers.validators import validateEmail



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users(request, format=None):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        raise('Only a get request may be performed on this endpoint')

@api_view(['GET'])
def get_home(request, format=None):
    return Response("Hello this is the api home")

@api_view(['POST'])
def create_user(request, format=None):
    ''' TODO: 
            1.) check if email is unique
            2.) check if email fits requirments (client side)

    '''
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        if (validateEmail(email)):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            serializer = UserSerializer(user, many=False)
            return Response({'status': '201',
                            'payload': serializer.data})
        else:
            raise(ValidationError('Email is not valid'))

# Need to create user_login, user_logout etc...
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, format=None):
    if request.method == 'GET':
        userID = int(request.GET.get('user_id', None))
        user = get_object_or_404(User, pk=userID)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    else:
        raise('Only a GET request may be performed on this endpoint')