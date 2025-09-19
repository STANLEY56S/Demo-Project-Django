from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .serializers import (
    AuthSerializer, CategorySerializer, ItemSerializer, 
    SignupSerializer, LoginSerializer, LogoutSerializer, ForgotPasswordSerializer,
    ChangePasswordSerializer
)
from .models import Auth, Category, Item


class AuthView(generics.ListCreateAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again.{}".format(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class AuthRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = AuthSerializer(instance, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again.{}".format(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({"detail": "Deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again.{}".format(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["id"]

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again."}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = CategorySerializer(instance, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again.{}".format(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({"detail": "Deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again.{}".format(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["id"]
    
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again."}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)



class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = ItemSerializer(instance, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again.{}".format(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response({"detail": "Deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Oops! Something went wrong. Please try again.{}".format(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignupAPIView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = []

    def created(self, request, *args, **kwargs):
        try:
            password = request.data.get('password', None)
            confirm_password = request.data.get('confirm_password', None)

            if password == confirm_password:
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response("message: Logging Success", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception=False)
            
            username = serializer.data.get('username', None)
            password = serializer.data.get('password', None)
            
            user = authenticate(username = username, password = password)

            if user:
                refresh_token = RefreshToken.for_user(user)
                access_token = refresh_token.access_token
                return Response({**serializer.data, "refresh_token" :str(refresh_token), "access_token" :str(access_token)}, status=status.HTTP_200_OK)
            else:
                return Response( {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED )
        except Exception as e:
            return Response({"error":e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception=False)
            refresh_token = serializer.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout Successfull"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ForgotPasswordAPIView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception=False)

            username = serializer.data.get('username', None)
            password = serializer.data.get('password', None)

        
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChangePasswordAPIView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception=True)
            user = request.user
            if user.check_password(serializer.data['old_password']):
                user.set_password(serializer.validated_data['password'])
                user.save()
                return Response({"message": "Password Change Success Fully. "}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("--------")
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

