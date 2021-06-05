from django.urls import path
from . import views

urlpatterns = [
    path('generatereport/', views.api_generate_report, name='api_generate_report'),
    path('getorders/',views.api_get_orders,name='api_get_orders'),
    path('viewallreports/',views.api_view_all_reports,name='api_view_all_reports'),
    path('filterreport/',views.api_filter_report,name='api_api_filter_report'),
    path('getreportbyid/<id>/', views.api_get_backtest_report_by_id, name='api_get_backtest_report_by_id'),
	path('getordersbyreportid/<id>/', views.api_get_orders_by_report_id, name='api_get_orders_by_report_id'),
    path('<slug>/', views.api_index, name='api_index')
]
