from django.core.cache import cache
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
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

        # Create new parameters
        Parameter.objects.create(a=a, b=b, total=total)
        return Response({'result': total})


class GetParamsHistoryAPIView(APIView):
    """Get parameters history API view."""
    serializer_class = ParamsHistorySerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ApiWrongMethodThrottle]

    def get(self, request):
        params_objects = cache.get('history_params_objects')
        print('read params_objects from cache')
        if params_objects is None:
            params_objects = Parameter.objects.all()
            cache.set('history_params_objects', params_objects)
            print('write params_objects to cache')
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
            print('total = read params_objects from cache')
        if params_objects is None:
            params_objects = Parameter.objects.all()
            cache.set('total_params_objects', params_objects)
            print('total = write params_objects to cache')
        serializer = self.serializer_class(params_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)