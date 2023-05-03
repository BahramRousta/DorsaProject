from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle
from .serializers import ParametersSerializer


class SumThrottle(UserRateThrottle):
    """
    Throttle the number of requests per hour for the CalculateSum api view
    """
    scope ='sum'


class ApiWrongMethodThrottle(SimpleRateThrottle):
    """
    Throttle the number of requests per hour with the wrong method and wrong params
    """
    scope = 'wrong_method_params'
    rate = '3/hour'

    def get_cache_key(self, request, view):

        # Only apply throttling to requests with the wrong method and wrong params
        if request.method in view.allowed_methods:
            if not request.query_params:
                return True
            elif ParametersSerializer(data=request.query_params).is_valid():
                return True
            else:
                return self.cache_format % {
                    'scope': self.scope,
                    'ident': self.get_ident(request)
                }
        else:
            return self.cache_format % {
                'scope': self.scope,
                'ident': self.get_ident(request)
            }

    def allow_request(self, request, view):

        if request.method in view.allowed_methods:
            if not request.query_params:
                return True
            elif ParametersSerializer(data=request.query_params).is_valid():
                return True
            else:
                return super().allow_request(request, view)
        else:
            return super().allow_request(request, view)