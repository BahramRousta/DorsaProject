from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    ParametersSerializer,
    ParamsHistorySerializer,
    TotalParametersSerializer
)
from .models import Parameter


class CalculateParamsAPIView(APIView):
    """Parameters API view."""
    serializer_class = ParametersSerializer

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

    def get(self, request):
        params = Parameter.objects.all()
        serializer = self.serializer_class(params, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetTotalParamsAPIView(APIView):
    """Get parameters history API view."""
    serializer_class = TotalParametersSerializer

    def get(self, request):
        params = Parameter.objects.all()
        print(params)
        serializer = self.serializer_class(params, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)