from django.urls import path
from . import views

urlpatterns = [
    path('listcompanies/', views.api_list_companies, name='api_list_companies'),
	path('<slug>/', views.api_index, name='api_index'),
]
