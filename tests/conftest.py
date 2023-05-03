import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import CustomUser


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def parameters_data():
    return {'a': 3, 'b': 4}


@pytest.fixture
def user_factory():
    return CustomUser.objects.create(username='username', password='password')