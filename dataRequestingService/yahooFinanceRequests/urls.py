from django.urls import path

from .views import StockViewSet

urlpatterns = [
    path('yahooFinanceRequests', StockViewSet.as_view({
        'post': 'getStockDataByKeyWords'
    }))
]