from django.urls import path
from . import views

urlpatterns = [
    path('dataondemand/', views.api_get_data_on_demand, name='api_get_data_on_demand'),
    path('derivecandle/', views.api_derive_candle_stick, name='api_derive_candle_stick'),
    path('getderivecandlestick/', views.api_get_candlestick_data, name='api_get_candlestick_data'),
    path('listcompanies/', views.api_list_companies, name='api_list_companies'),
    path('indicatorsdata/', views.api_get_indicators_data, name='api_get_indicator_data'),
    path('<slug>/', views.api_index, name='api_index'),
]
