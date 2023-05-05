from unittest.mock import patch

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import CustomUser


@pytest.mark.django_db
@patch('app.throttles.DataWrongThrottle.allow_request', return_value=True)
@patch('app.throttles.ApiWrongMethodThrottle.allow_request', return_value=True)
@patch('app.throttles.WrongQueryParamsThrottle.allow_request', return_value=True)
def test_login_api_view(mock_throttle1, mock_throttle2, mock_throttle3, api_client):
    # Create a user for testing
    user = CustomUser.objects.create_user(username='testuser', password='testpass')

    # Define the login URL and request data
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'testpass'
    }

    # Make a POST request to the login endpoint
    response = api_client.post(url, data, format='json')

    # Check that the response status code is 200 OK
    assert response.status_code == status.HTTP_200_OK

    assert 'access_token' in response.data
    assert 'refresh_token' in response.data
    assert user.is_authenticated