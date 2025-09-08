from rest_framework import serializers
from .models import Auth, Category, Item, BaseUser
from django.contrib.auth.hashers import make_password

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ["id", "username", "email", "password"]
        
    def create(self, validated_data):
        
        password = make_password(validated_data['password'])
        
        user = BaseUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            password = password
        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ["id", "username", "password"]

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    password = serializers.CharField()

class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ["username", "password"]
