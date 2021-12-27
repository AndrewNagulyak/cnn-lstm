from django.urls import path

from .views import CorrelationViewSet

urlpatterns = [
    path('correlationAnalys', CorrelationViewSet.as_view({
        'post': 'getCorrelationAnalys'
    }))
]