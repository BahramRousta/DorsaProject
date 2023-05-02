from django.urls import path
from .views import CalculateParamsAPIView

urlpatterns = [
    path('sum/', CalculateParamsAPIView.as_view(), name='sum'),
]