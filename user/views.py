from django.contrib.auth import login
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import CustomUser
from user.serializers import LoginSerializer, ObtainTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from log.user_logger import user_logger


class LoginAPIView(APIView):
    """Login API View. Receive username and password. Return access and refresh token."""
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def _obtain_token(self, request, user):
        """Return access and refresh token for user."""

        try:
            refresh = RefreshToken.for_user(user)
            token = ObtainTokenSerializer({
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)
            }).data
            user_logger.info(f"Token generated for {user.username} - {__name__}.")
            return token
        except Exception as e:
            user_logger.error(f"Failed to generate token for {user.username} - {__name__}.")
            raise e

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            # Get user from DB
            user = CustomUser.objects.filter(username=data["username"]).first()

            # Validate password
            if user and user.check_password(data["password"]):
                login(request, user)
                user_logger.info(f"User {user.username} logged in successfully - {__name__} - {request.path}")
                return Response(
                    status=status.HTTP_200_OK,
                    data=self._obtain_token(request, user)
                )
            else:
                user_logger.error(f"User login failed. - {__name__} - {request.path}")
                return Response(
                    status=status.HTTP_403_FORBIDDEN,
                    data={"Message": "The user information is invalid."}
                )
        else:
            user_logger.error(f"User data is not valid. - {__name__} - {request.path}")
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )
