from django.urls import path
from . import views

urlpatterns = [
    path('getbacktests',views.api_listbacktests, name='api_listbacktests'),
    path('getreports/<id>/',views.api_listreports,name='api_listreports'),
    path('<slug>/', views.api_index, name='api_index')
]
