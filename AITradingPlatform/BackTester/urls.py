from django.urls import path
from . import views

urlpatterns = [
    path('generatereport/', views.api_generate_report, name='api_generate_report'),
    path('getorders/',views.api_get_orders,name='api_get_orders'),
    path('viewallreports/',views.api_view_all_reports,name='api_view_all_reports'),
    path('filterreport/',views.api_filter_report,name='api_api_filter_report'),
    path('<slug>/', views.api_index, name='api_index')
]
