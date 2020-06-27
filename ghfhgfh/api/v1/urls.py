from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FfghhgfjViewSet

router = DefaultRouter()
router.register("ffghhgfj", FfghhgfjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
