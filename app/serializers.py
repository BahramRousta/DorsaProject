from rest_framework import serializers


class ParametersSerializer(serializers.Serializer):
    """Serializer for parameters"""

    a = serializers.FloatField()
    b = serializers.FloatField()
