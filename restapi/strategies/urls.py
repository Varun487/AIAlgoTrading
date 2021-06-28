from django.urls import path
from . import views

urlpatterns = [
    path('allstrategies/', views.api_get_all_strategies, name='api_get_all_strategies'),
    path('strategydata/<int:strategy_id>/', views.api_get_strategy_data, name='api_get_strategy_data'),
    path('<slug>/', views.api_index, name='api_index'),
]
