import pytest
from rest_framework.exceptions import ValidationError as DRFValidationError
from decimal import Decimal
from app.serializers import ParametersSerializer, ParamsHistorySerializer, TotalParametersSerializer


class TestParametersSerializer:

    def test_parameters_serializer_valid(self, valid_data):
        serializer = ParametersSerializer(data=valid_data)
        assert serializer.is_valid()

    def test_parameters_serializer_invalid(self, invalid_data):
        serializer = ParametersSerializer(data=invalid_data)
        with pytest.raises(DRFValidationError):
            serializer.is_valid(raise_exception=True)


class TestParamsHistorySerializer:

    @pytest.mark.django_db
    def test_params_history_serializer(self, params_factory):
        serializer = ParamsHistorySerializer(instance=params_factory)
        assert serializer.data == {'a': 2.5, 'b': 3.5}


class TestTotalParametersSerializer:

    @pytest.mark.django_db
    def test_total_parameters_serializer(self, params_factory):
        serializer = TotalParametersSerializer(instance=params_factory)
        assert serializer.data == {'total': Decimal('6.0')}