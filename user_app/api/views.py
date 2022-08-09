from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
from rest_framework import status

from django.contrib.auth.models import User 

from user_app.api.serializers import RegistrationSerializer
from user_app import models


@api_view(['POST'])
def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        

@api_view(['POST'])
def registration_view(request):
    if request.method == "POST":
        serializers = RegistrationSerializer(data=request.data)
        data = {}

        if serializers.is_valid():
            account = serializers.save()
            data['response'] = 'Registration Successful!'
            data['username'] = account.username 
            data['email'] = account.email
            data['token'] = Token.objects.get(user=account).key 
        else:
            data = serializers.errors 

        return Response(data)
        