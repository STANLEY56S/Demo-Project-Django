from rest_framework.routers import DefaultRouter
from .views import (
    AuthViewSet, CategoryViewSet, ItemViewSet,
    SignupViewSet, LoginViewSet, LogoutViewSet, ChangePasswordViewSet
)

router = DefaultRouter()
router.register("auth", AuthViewSet)
router.register("category", CategoryViewSet)
router.register("item", ItemViewSet)
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("logout", LogoutViewSet, basename="logout")
router.register("change-password", ChangePasswordViewSet, basename="change-password")

urlpatterns = router.urls
