from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle
from .serializers import ParametersSerializer


class SumThrottle(UserRateThrottle):
    """
    Throttle the number of requests per hour for the CalculateSum api view
    """
    scope ='sum'


class ApiMethodThrottle(SimpleRateThrottle):
    """
    Throttle the number of requests per hour with the wrong method
    """
    scope = 'wrong_method'

    def get_cache_key(self, request, view):
        # Only apply throttling to requests with the wrong method
        if request.method in view.allowed_methods and ParametersSerializer(data=request.query_params).is_valid():
                return None
        else:
            return self.get_ident(request)

    def allow_request(self, request, view):
        # Only apply throttling to requests with the wrong method
        if request.method in view.allowed_methods and ParametersSerializer(data=request.query_params).is_valid():
                return True

        # Check if the client has exceeded the rate limit
        self.rate = self.get_rate()
        self.num_requests, self.duration = self.parse_rate(self.rate)
        self.key = self.get_cache_key(request, view)
        self.history = self.cache.get(self.key, [])
        self.now = self.timer()
        self.history.insert(0, self.now)
        self.history = self.history[:self.num_requests]
        if len(self.history) >= self.num_requests:
            if self.history[-1] >= self.now - self.duration:
                return False

        self.cache.set(self.key, self.history, self.duration)
        return True