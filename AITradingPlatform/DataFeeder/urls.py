from django.urls import path
from . import views

urlpatterns = [
    path('dataondemand/', views.api_get_data_on_demand, name='api_get_data_on_demand'),
    path('listcompanies/', views.api_list_companies, name='api_list_companies'),
	path('<slug>/', views.api_index, name='api_index'),
    path('derivedindicatorcalc/',views.calcderievedindiactor,name='calcderievedindicator'),
]
