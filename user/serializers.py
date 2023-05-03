from rest_framework import serializers
from core.settings import SIMPLE_JWT


class LoginSerializer(serializers.Serializer):
    """Serializer for login request"""

    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )


class ObtainTokenSerializer(serializers.Serializer):
    """Serializer for user authentication"""

    access_token = serializers.CharField(max_length=255)
    access_token_expiration = serializers.CharField(
        default=f"{SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds} seconds"
    )
    refresh_token = serializers.CharField(max_length=255)
    refresh_token_expiration = serializers.CharField(
        default=f"{SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds()} seconds"
    )