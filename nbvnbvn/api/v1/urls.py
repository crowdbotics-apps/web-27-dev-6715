from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FgghhjgViewSet

router = DefaultRouter()
router.register("fgghhjg", FgghhjgViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
