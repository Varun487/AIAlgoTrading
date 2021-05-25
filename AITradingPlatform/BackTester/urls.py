from django.urls import path
from . import views

urlpatterns = [
    path('generatereport/', views.api_generate_report, name='api_generate_report'),
    path('<slug>/', views.api_index, name='api_index')
]
