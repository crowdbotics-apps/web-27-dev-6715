from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SkjlkjljViewSet

router = DefaultRouter()
router.register("skjlkjlj", SkjlkjljViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
