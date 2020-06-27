from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SgyytViewSet

router = DefaultRouter()
router.register("sgyyt", SgyytViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
