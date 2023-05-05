from django.utils import timezone
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, SimpleRateThrottle
from .serializers import ParametersSerializer


class SumAnonymousRateThrottle(AnonRateThrottle):
    """
    Throttle the number of requests per hour for the CalculateSum api view
    """
    scope = 'sum_anon'
    rate = '100/hour'


class SumUserRateThrottle(UserRateThrottle):
    """
    Throttle the number of requests per hour for the CalculateSum api view
    """
    scope = 'sum_user'
    rate = '100/hour'


class ApiWrongMethodThrottle(SimpleRateThrottle):
    """
    Throttle the number of requests per hour with the wrong method
    """
    scope = 'wrong_method_params'

    def __init__(self):
        self.history = []
        super().__init__()

    def get_cache_key(self, request, view):
        if request.method not in view.allowed_methods:
            # throttle user for 1 hour
            self.cache.set(self.get_ident(request) + '-wrong_method_params', timezone.now(), 3600)
            return self.get_ident(request) + '-wrong_method_params', 3600
        else:
            cache_key = self.get_ident(request) + '-wrong_method_params'
            throttle_time = self.cache.get(cache_key)
            if throttle_time is not None:
                time_elapsed = (timezone.now() - throttle_time).total_seconds()
                if time_elapsed < 3600:
                    self.wait()
                    return cache_key, 3600
                else:
                    self.cache.delete(cache_key)
            return None


class DataWrongThrottle(UserRateThrottle):
    """
    Throttle the number of requests per hour with the wrong data
    """
    scope = 'data_wrong'

    def __init__(self):
        self.history = []
        super().__init__()

    def get_cache_key(self, request, view):
        if not request.query_params or not ParametersSerializer(data=request.query_params).is_valid():
            # throttle user for 1 hour
            self.cache.set(self.get_ident(request) + '-data_wrong', timezone.now(), 3600)
            return self.get_ident(request) + '-data_wrong', 3600

        else:
            cache_key = self.get_ident(request) + '-data_wrong'
            throttle_time = self.cache.get(cache_key)
            if throttle_time is not None:
                time_elapsed = (timezone.now() - throttle_time).total_seconds()
                if time_elapsed < 3600:
                    self.wait()
                    return cache_key, 3600
                else:
                    self.cache.delete(cache_key)
            return None


class WrongQueryParamsThrottle(UserRateThrottle):
    """
    Throttle the number of requests per hour with the wrong data
    """
    scope = 'query_wrong'

    def __init__(self):
        self.history = []
        super().__init__()

    def get_cache_key(self, request, view):
        if request.query_params:
            # throttle user for 1 hour
            self.cache.set(self.get_ident(request) + '-query_wrong', timezone.now(), 3600)
            return self.get_ident(request) + '-query_wrong', 3600

        else:
            cache_key = self.get_ident(request) + '-query_wrong'
            throttle_time = self.cache.get(cache_key)
            if throttle_time is not None:
                time_elapsed = (timezone.now() - throttle_time).total_seconds()
                if time_elapsed < 3600:
                    self.wait()
                    return cache_key, 3600
                else:
                    self.cache.delete(cache_key)
            return None