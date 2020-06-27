from rest_framework import authentication
from nbvnbvn.models import Fgghhjg
from .serializers import FgghhjgSerializer
from rest_framework import viewsets


class FgghhjgViewSet(viewsets.ModelViewSet):
    serializer_class = FgghhjgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Fgghhjg.objects.all()
