from django.urls import path
from . import views
import dashboard

app_name = "dashboard"

urlpatterns = [
    path('',views.DashboardView.as_view(),name="index"),
    path('currencies/',views.CurrencyListView.as_view(),name="currency-list"),
    path('currencies/add/',views.RegisterCurrencyCreateView.as_view(),name="currency-add"),

    path('stocks/',views.StockListView.as_view(),name="stock-list"),
    path('stoock/add/',views.RegisterStockCreateView.as_view(),name="stock-add"),

    path('futures/',views.FuturesListView.as_view(),name="futures-list"),
    path('futures/add',views.RegisterFutureCreateView.as_view(),name="futures-add"),
    
    path('cryptos/',views.CryptoListView.as_view(),name="cryto-list"),
    path('cryptos/add',views.RegisterCryptoCreateView.as_view(),name="cryto-add"),
    path('data-line/currency/',views.population_chart,name="linechart"),
]
