from django.urls import path
from .views import (
    CalculateParamsAPIView,
    GetParamsHistoryAPIView,
    GetTotalParamsAPIView
)

urlpatterns = [
    path('sum/', CalculateParamsAPIView.as_view(), name='sum'),
    path('history/', GetParamsHistoryAPIView.as_view(), name='history'),
    path('total/', GetTotalParamsAPIView.as_view(), name='total'),
]