from unittest import mock
from unittest.mock import patch, MagicMock
import pytest
from django.core.cache import cache
from django.urls import reverse
from rest_framework import status
from app.models import Parameter
from app.views import (
    CalculateSumParamsAPIView,
    GetParamsHistoryAPIView,
    GetTotalParamsAPIView,
)


@pytest.mark.django_db
class TestCalculateSumParamsAPIView:

    @classmethod
    def setup_method(cls):
        cls.url = reverse('sum')

    def test_calculate_sum_params_api_view_success(self, api_client, parameters_data):
        CalculateSumParamsAPIView.throttle_classes = [MagicMock()]
        CalculateSumParamsAPIView.permission_classes = [MagicMock()]

        response = api_client.get(self.url, parameters_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {'result': 7}

    def test_calculate_sum_params_api_view_missing_parameters(self, api_client):
        GetParamsHistoryAPIView.throttle_classes = [MagicMock()]
        GetParamsHistoryAPIView.permission_classes = [MagicMock()]

        response = api_client.get(self.url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestGetParamsHistoryAPIView:

    @classmethod
    def setup_method(cls):
        cls.url = reverse('history')

    def test_get_params_history_api_view_success(self, api_client, user_factory):
        GetParamsHistoryAPIView.throttle_classes = [MagicMock()]
        GetParamsHistoryAPIView.permission_classes = [MagicMock()]

        user = user_factory
        api_client.force_authenticate(user=user)

        response = api_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK

    def test_get_params_history_api_view_with_cache(self, api_client, user_factory):
        GetParamsHistoryAPIView.throttle_classes = [MagicMock()]
        GetParamsHistoryAPIView.permission_classes = [MagicMock()]

        Parameter.objects.create(a=1, b=2, total=3)
        Parameter.objects.create(a=4, b=5, total=9)

        user = user_factory
        api_client.force_authenticate(user=user)

        cache.set('history_params_objects', Parameter.objects.all())
        with patch('app.views.app_logger.info') as mock_logger:
            response = api_client.get(self.url)

            assert response.status_code == status.HTTP_200_OK
            mock_logger.assert_called_with('Params history get from cache = app.views - /history/')

    def test_get_params_history_api_view_without_cache(self, api_client, user_factory):
        GetParamsHistoryAPIView.throttle_classes = [MagicMock()]
        GetParamsHistoryAPIView.permission_classes = [MagicMock()]

        cache.delete('history_params_objects')

        user = user_factory
        api_client.force_authenticate(user=user)

        with patch('app.views.app_logger.info') as mock_logger:
            response = api_client.get(self.url)

            assert response.status_code == status.HTTP_200_OK
            mock_logger.assert_called_with('Params history write into cache = app.views - /history/')


@pytest.mark.django_db
class TestGetTotalParamsAPIView:

    @classmethod
    def setup_method(cls):
        cls.url = reverse('total')

    def test_get_total_params_history_api_view_success(self, api_client, user_factory):
        GetTotalParamsAPIView.throttle_classes = [MagicMock()]
        GetTotalParamsAPIView.permission_classes = [MagicMock()]

        user = user_factory
        api_client.force_authenticate(user=user)

        response = api_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK

    def test_get_total_params_history_api_view_with_cache(self, api_client, user_factory):
        GetTotalParamsAPIView.throttle_classes = [MagicMock()]
        GetTotalParamsAPIView.permission_classes = [MagicMock()]

        Parameter.objects.create(a=1, b=2, total=3)
        Parameter.objects.create(a=4, b=5, total=9)

        user = user_factory
        api_client.force_authenticate(user=user)

        cache.set('total_params_objects', Parameter.objects.all())

        with patch('app.views.app_logger.info') as mock_logger:
            response = api_client.get(self.url)

            assert response.status_code == status.HTTP_200_OK
            mock_logger.assert_called_with('Total history get from cache = app.views - /total/')

    def test_get_total_params_history_api_view_without_cache(self, api_client, user_factory):
        GetTotalParamsAPIView.throttle_classes = [MagicMock()]
        GetTotalParamsAPIView.permission_classes = [MagicMock()]

        cache.delete('total_params_objects')

        user = user_factory
        api_client.force_authenticate(user=user)

        with patch('app.views.app_logger.info') as mock_logger:
            response = api_client.get(self.url)

            assert response.status_code == status.HTTP_200_OK
            mock_logger.assert_called_with('Total history write into cache = app.views - /total/')