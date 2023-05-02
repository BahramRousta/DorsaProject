from rest_framework import serializers
from .models import Parameter


class ParametersSerializer(serializers.Serializer):
    """Serializer for parameters"""

    a = serializers.FloatField()
    b = serializers.FloatField()


class ParamsHistorySerializer(serializers.ModelSerializer):
    """Serializer for parameters history"""

    class Meta:
        model = Parameter
        fields = ('a', 'b')


class TotalParametersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parameter
        fields = ('total',)

