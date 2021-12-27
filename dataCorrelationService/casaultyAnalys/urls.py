from django.urls import path

from .views import CasaultyViewSet

urlpatterns = [
    path('casaultyAnalys', CasaultyViewSet.as_view({
        'post': 'getCasaultyAnalys'
    }))
]