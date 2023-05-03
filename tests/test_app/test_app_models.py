import pytest
from django.utils import timezone
from app.models import Parameter


class TestParameterModel:

    @pytest.mark.django_db
    def test_should_create_new_parameter_obj(self):
        parameter = Parameter.objects.create(a=2.5, b=3.5, total=6.0)

        assert Parameter.objects.count() == 1
        assert parameter.created_at <= timezone.now()

    @pytest.mark.django_db
    def test_parameter_str_method(self):
        parameter = Parameter.objects.create(a=2.5, b=3.5, total=6.0)

        assert str(parameter) == '2.5 + 3.5 = 6.0'