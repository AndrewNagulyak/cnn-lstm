from django.urls import path

from .views import TwitterViewSet

urlpatterns = [
    path('twitterRequests', TwitterViewSet.as_view({
        'post': 'getTwitterDataByKeyWords'
    }))
]