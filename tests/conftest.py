import pytest
from rest_framework.test import APIClient

from app.models import Parameter
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


@pytest.fixture
def params_factory():
    return Parameter.objects.create(a=2.5, b=3.5, total=6.0)


@pytest.fixture
def valid_data():
    return {
        'a': 2.5,
        'b': 3.5
    }


@pytest.fixture
def invalid_data():
    return {
        'a': 'invalid_value',
        'b': 3.5
    }