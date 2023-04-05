from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework .decorators import APIView
from . Serializers import UserSigninSerializer,UserSignupSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
# Create your views here.




class UserSignin(APIView):
     def post(self,request,format=None):
        user = authenticate(username=request.data['username'],password=request.data['password'])
        if user:
            token = RefreshToken.for_user(user)
            return Response({
                  'refresh': str(token),
                  'access': str(token.access_token),
            })
        else:
            return Response({
                'Error':"Something wromg here"
            })

class UserSignUp(APIView):
    def post(self,request,format=None):
        data = request.data
        data['password'] = make_password(request.data['password'])
        serializer = UserSignupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = RefreshToken.for_user(user)
            return Response({
                  'refresh': str(token),
                  'access': str(token.access_token),
            })
        else:
            return Response({
                'Error':"Something wromg here"
            })
            