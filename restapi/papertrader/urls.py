from django.urls import path
from . import views

urlpatterns = [
    path('allpapertrades/<int:strategy_type_id>/', views.api_get_all_papertrades, name='api_get_all_papertrades'),
    path('papertradedata/<int:papertrade_id>/', views.api_get_papertrade_data, name='api_get_papertrade_data'),
    path('companyquote/<int:papertrade_id>/', views.api_get_company_quote, name='api_get_company_quote'),
    path('papertradevisualization/<int:papertrade_id>/', views.api_get_paper_trade_visualization,
         name='api_get_paper_trade_visualization'),
    path('<slug>/', views.api_index, name='api_index'),
]
