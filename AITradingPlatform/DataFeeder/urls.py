from django.urls import path
from . import views

urlpatterns = [
    path('dataondemand/', views.api_get_data_on_demand, name='api_get_data_on_demand'),
    path('listcompanies/', views.api_list_companies, name='api_list_companies'),
    path('indicatorsdata/', views.api_get_indicators_data, name='api_get_indicator_data'),
    path('derivedindicatorcalc/',views.calcderievedindiactor,name='calcderievedindiactor'),
    path('<slug>/', views.api_index, name='api_index'),
    
]
