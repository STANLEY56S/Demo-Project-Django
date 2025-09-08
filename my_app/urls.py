from django.urls import path, include
from .views import (
    
    AuthView, AuthRetrieveUpdateDestroyView, 
    CategoryView, CategoryRetrieveUpdateDestroyView,
    ItemView, ItemRetrieveUpdateDestroyView, 
    
    SignupAPIView, LoginAPIView, LogoutAPIView, ForgotPasswordAPIView, ChangePasswordAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("auth/", AuthView.as_view()),
    path("category/", CategoryView.as_view()),
    path("item/", ItemView.as_view()),

    path("auth/<int:id>", AuthRetrieveUpdateDestroyView.as_view()),
    path("category/<int:id>", CategoryRetrieveUpdateDestroyView.as_view()),
    path("item/<int:id>", ItemRetrieveUpdateDestroyView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("regester/",SignupAPIView.as_view()),
    path("do_login/",LoginAPIView.as_view()),
    path("logout/",LogoutAPIView.as_view()),
    path("Forgot_Password/",ForgotPasswordAPIView.as_view()),
    path("change_password/",ChangePasswordAPIView.as_view()),
    
    
]
