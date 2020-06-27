from rest_framework import authentication
from nbvnbv.models import Skjlkjlj
from .serializers import SkjlkjljSerializer
from rest_framework import viewsets


class SkjlkjljViewSet(viewsets.ModelViewSet):
    serializer_class = SkjlkjljSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Skjlkjlj.objects.all()
