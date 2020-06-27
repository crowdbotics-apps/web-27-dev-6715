from rest_framework import authentication
from ghfhgfh.models import Ffghhgfj
from .serializers import FfghhgfjSerializer
from rest_framework import viewsets


class FfghhgfjViewSet(viewsets.ModelViewSet):
    serializer_class = FfghhgfjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ffghhgfj.objects.all()
