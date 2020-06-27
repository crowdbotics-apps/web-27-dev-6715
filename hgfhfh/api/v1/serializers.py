from rest_framework import serializers
from hgfhfh.models import Sgyyt


class SgyytSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sgyyt
        fields = "__all__"
