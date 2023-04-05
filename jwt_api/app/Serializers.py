from rest_framework import serializers
from django.contrib.auth.models import User

class UserSigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        
class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']


        