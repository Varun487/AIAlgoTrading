from django.urls import path
from . import views

urlpatterns = [
    path('getstrategies/', views.api_list_strategy, name='api_list_strategy'),
    path('getpapertradeorders/', views.api_list_PaperTradeOrder, name='api_list_PaperTradeOrder'),
    path('<slug>/', views.api_index, name='api_index')
]
