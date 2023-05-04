import pytest
from django.urls import reverse
from rest_framework import status


class TestThrottles:

    @pytest.mark.django_db
    def test_sum_throttle(self, api_client, parameters_data):
        """
        Test that the CalculateSum API view is throttled
        """

        url = reverse('sum')
        for i in range(101):
            api_client.get(url, parameters_data)

        response = api_client.get(url, parameters_data)
        assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS

    @pytest.mark.django_db
    def test_api_wrong_method_throttle(self, api_client, parameters_data, user_factory):
        """
        Test that the CalculateSum API view is throttled
        """
        user = user_factory
        api_client.force_authenticate(user)
        url = reverse('total')

        for i in range(10):
            api_client.post(url, parameters_data)

        response = api_client.post(url)
        assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS
