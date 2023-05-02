from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ParametersSerializer
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
        Parameter.objects.create(params={
            "a": a,
            "b": b,
            "total": total
        })

        return Response({'result': total})