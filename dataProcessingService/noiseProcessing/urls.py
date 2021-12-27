from django.urls import path

from .views import TwitterProcessingViewSet

urlpatterns = [
    path('noiseProcessing', TwitterProcessingViewSet.as_view({
        'post': 'processTwitterData'
    }))
]