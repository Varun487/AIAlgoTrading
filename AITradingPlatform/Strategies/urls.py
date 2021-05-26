from django.urls import path
from . import views

urlpatterns = [
    path('runstrategy/', views.api_run_strategy, name='api_run_strategy'),
    path('getstrategies/', views.api_get_strategy, name='api_get_strategy'),
    path('<slug>/', views.api_index, name='api_index'),
]
