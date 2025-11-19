from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import Auth, Category, Item
from .serializers import (
    AuthSerializer, CategorySerializer, ItemSerializer,
    SignupSerializer, LoginSerializer, LogoutSerializer,
    ForgotPasswordSerializer, ChangePasswordSerializer
)
from common.Response import ResponseCode


# BASE GENERIC FUNCTIONS
def save_response(serializer):
    if serializer.is_valid():
        serializer.save()
        return ResponseCode.create_response("SAVE_SUCCESSFULLY", data=serializer.data)
    return ResponseCode.create_response("INVALID_DATA", data=serializer.errors)


def update_response(serializer):
    if serializer.is_valid():
        serializer.save()
        return ResponseCode.create_response("UPDATE_SUCCESSFULLY", data=serializer.data)
    return ResponseCode.create_response("INVALID_DATA", data=serializer.errors)


# AUTH VIEWSET
class AuthViewSet(viewsets.ModelViewSet):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["id"]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            return save_response(serializer)
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return ResponseCode.create_response("FETCH_SUCCESSFULLY", data=serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            return update_response(serializer)
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return ResponseCode.create_response("DELETE_SUCCESSFULLY")
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))


# CATEGORY VIEWSET
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["id"]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            return save_response(serializer)
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return ResponseCode.create_response("FETCH_SUCCESSFULLY", data=serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            return update_response(serializer)
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return ResponseCode.create_response("DELETE_SUCCESSFULLY")
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))


# ITEM VIEWSET
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["id"]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            return save_response(serializer)
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return ResponseCode.create_response("FETCH_SUCCESSFULLY", data=serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            return update_response(serializer)
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return ResponseCode.create_response("DELETE_SUCCESSFULLY")
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))


# AUTHENTICATION - VIEWSET STYLE
class SignupViewSet(viewsets.ViewSet):
    permission_classes = []

    def create(self, request):
        try:
            serializer = SignupSerializer(data=request.data)
            return save_response(serializer)
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))


class LoginViewSet(viewsets.ViewSet):
    permission_classes = []

    def create(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid()

            username = serializer.data.get("username")
            password = serializer.data.get("password")

            user = authenticate(username=username, password=password)
            if not user:
                return ResponseCode.create_response("INVALID_CREDENTIALS")

            refresh = RefreshToken.for_user(user)
            data = {
                "username": username,
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            }
            return ResponseCode.create_response("FETCH_SUCCESSFULLY", data=data)

        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))


class LogoutViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = LogoutSerializer(data=request.data)
            serializer.is_valid()

            token = RefreshToken(serializer.data["refresh_token"])
            token.blacklist()

            return ResponseCode.create_response("UPDATE_SUCCESSFULLY", message="Logged out successfully")

        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))


class ChangePasswordViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = ChangePasswordSerializer(data=request.data)
            serializer.is_valid()

            user = request.user
            if not user.check_password(serializer.data["old_password"]):
                return ResponseCode.create_response("INVALID_DATA", message="Incorrect old password")

            user.set_password(serializer.data["password"])
            user.save()

            return ResponseCode.create_response("UPDATE_SUCCESSFULLY", message="Password changed")
        except Exception as e:
            return ResponseCode.create_response("SERVER_ERROR", message=str(e))
