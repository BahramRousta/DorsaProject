from django.core.cache import cache
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from log.app_logger import app_logger
from .serializers import (
    ParametersSerializer,
    ParamsHistorySerializer,
    TotalParametersSerializer
)
from .models import Parameter
from .throttles import ApiWrongMethodThrottle, SumThrottle


class CalculateSumParamsAPIView(APIView):
    """Parameters API view."""
    serializer_class = ParametersSerializer
    permission_classes = [AllowAny]
    throttle_classes = [ApiWrongMethodThrottle, SumThrottle]

    def get(self, request):

        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        # Get parameters
        a = serializer.data.get('a', None)
        b = serializer.data.get('b', None)

        # Calculate the parameter
        total = (a + b)
        app_logger.info(f'Total calculated = {total}, {__name__} - {request.path}')

        # Create new parameters
        try:
            Parameter.objects.create(a=a, b=b, total=total)
            app_logger.info(f'Created new parameters from {a} + {b}, {__name__} - {request.path}')
            return Response({'result': total}, status=status.HTTP_201_CREATED)
        except Exception as e:
            app_logger.exception(e, __name__)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetParamsHistoryAPIView(APIView):
    """Get parameters history API view."""
    serializer_class = ParamsHistorySerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ApiWrongMethodThrottle]

    def get(self, request):
        params_objects = cache.get('history_params_objects')
        if params_objects:
            app_logger.info(f'History get from cache = {__name__} - {request.path}')
        if params_objects is None:
            params_objects = Parameter.objects.all()
            cache.set('history_params_objects', params_objects)
            app_logger.info(f'History write into cache = {__name__} - {request.path}')
        serializer = self.serializer_class(params_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetTotalParamsAPIView(APIView):
    """Get parameters history API view."""
    serializer_class = TotalParametersSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ApiWrongMethodThrottle]

    def get(self, request):
        params_objects = cache.get('total_params_objects')
        if params_objects:
            app_logger.info(f'Total history get from cache = {__name__} - {request.path}')
        if params_objects is None:
            params_objects = Parameter.objects.all()
            cache.set('total_params_objects', params_objects)
            app_logger.info(f'Total history write into cache = {__name__} - {request.path}')
        serializer = self.serializer_class(params_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)