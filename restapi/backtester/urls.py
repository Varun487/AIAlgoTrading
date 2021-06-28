from django.urls import path
from . import views

urlpatterns = [
    path('allbacktests/<int:strategy_type_id>/', views.api_get_all_backtests, name='api_get_all_backtests'),
    path('backtestdata/<int:backtest_id>/', views.api_get_backtest_data, name='api_get_backtest_data'),
    path('backtestsignalvisualization/<int:backtest_id>/', views.api_get_backtest_signal_visualization,
         name='api_get_backtest_signal_visualization'),

    path('allbacktesttrades/<int:backtest_id>/', views.api_get_all_backtest_trades, name='api_get_backtest_data'),
    path('backtesttradedata/<int:backtest_trade_id>/', views.api_get_backtest_trade_data, name='api_get_backtest_data'),
    path('backtesttradevisualization/<int:backtest_trade_id>/', views.api_get_backtest_trade_visualization,
         name='api_get_backtest_trade_visualization'),

    path('<slug>/', views.api_index, name='api_index')
]
