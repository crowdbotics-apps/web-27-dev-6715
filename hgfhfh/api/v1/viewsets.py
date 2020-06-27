from rest_framework import authentication
from hgfhfh.models import Sgyyt
from .serializers import SgyytSerializer
from rest_framework import viewsets


class SgyytViewSet(viewsets.ModelViewSet):
    serializer_class = SgyytSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Sgyyt.objects.all()
