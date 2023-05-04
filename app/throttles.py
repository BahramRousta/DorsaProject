from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle, AnonRateThrottle
from .serializers import ParametersSerializer


class SumAnonymousRateThrottle(AnonRateThrottle):
    """
    Throttle the number of requests per hour for the CalculateSum api view
    """
    scope = 'sum_anon'


class SumUserRateThrottle(UserRateThrottle):
    """
    Throttle the number of requests per hour for the CalculateSum api view
    """
    scope = 'sum_user'


class ApiWrongMethodThrottle(UserRateThrottle):
    """
    Throttle the number of requests per hour with the wrong method
    """
    scope = 'wrong_method_params'

    def allow_request(self, request, view):
        if request.method in view.allowed_methods:
            return True
        else:
            return super().allow_request(request, view)


class DataWrongThrottle(UserRateThrottle):
    """
    Throttle the number of requests per hour with the wrong data
    """
    scope = 'data_wrong'

    def allow_request(self, request, view):
        if not request.query_params or ParametersSerializer(data=request.query_params).is_valid():
            return True
        else:
            return super().allow_request(request, view)
