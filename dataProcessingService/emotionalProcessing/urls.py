from django.urls import path

from .views import EmotionalViewSet

urlpatterns = [
    path('emotionalProcessing', EmotionalViewSet.as_view({
        'post': 'processEmotionalData'
    }))
]